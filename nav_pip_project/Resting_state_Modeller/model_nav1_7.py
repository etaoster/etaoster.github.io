# use automodel to generate Nav1.7 resting state based on VSD templates specified

from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the AutoModel class

log.verbose()    # request verbose output
env = Environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = AutoModel(env,
              alnfile='align_nav1_7.ali',
              knowns=('7xve','7k48','6nt4','7w9k'),
              sequence='model_nav1_7',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))

a.starting_model = 1
a.ending_model = 50

a.md_level = refine.slow

a.make()


