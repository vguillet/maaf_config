
# >>>>>>>>>>>> ROS CONFIGURATION FILE
from .ros_pubsub_config import *

# >>>>>>>>>>>> FRAMEWORK CONFIGURATION FILE
ALLOCATION_METHOD = "I-CBBA"

DEBUG = False

# >>>>>>>>>> RUN MODES DEFINITION
SIM = 0
OPERATIONAL = 1

RUN_MODE = OPERATIONAL

if RUN_MODE == OPERATIONAL:
    pass

elif RUN_MODE == SIM:
    from .sim_config import *

# >>>>>>>>>> ORGANISATION CONFIGURATION FILE
organisation_file_path = "src/icare_alloc_config/icare_alloc_config/__cache/__CoHoMa_organisation_model_v1.json"

organisation_folder_path = "src/icare_alloc_config/icare_alloc_config"