import sys
import git
import pathlib

PROJ_ROOT_PATH = pathlib.Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
PROJ_ROOT =  str(PROJ_ROOT_PATH)
if PROJ_ROOT not in sys.path:
    sys.path.append(PROJ_ROOT)
    
import numpy as np
SEEDS_FOLDER = pathlib.Path(PROJ_ROOT_PATH / "seedfiles" )
pathlib.Path(SEEDS_FOLDER).mkdir(parents=True, exist_ok=True)

   
# Generate model seeds
def generate_seeds(root_seed=20241016, no_of_seeds=5):
    """
    Generates a set of random model seeds and saves them to a file.

    Parameters:
        root_seed (int): The seed for the random number generator.
        no_of_seeds (int): The number of seeds to generate.

    Returns:
        pathlib.Path: The path to the generated seeds file.
    """
    rng = np.random.default_rng(root_seed)
    print("Generating model seeds")
    seeds = sorted(rng.integers(low=1000, high=9999, size=no_of_seeds))
    seeds_filename = f"seeds-{root_seed}x{no_of_seeds}.dat"
    seeds_file = SEEDS_FOLDER / seeds_filename
    np.savetxt(seeds_file, seeds, fmt="%d")
    print(f"Seedfile saved at {seeds_file}")
    return seeds_file

# Load model seeds
def load_model_seeds(seeds_file):
    """
    Loads model seeds from a file.

    Parameters:
        seeds_file (pathlib.Path): The path to the seeds file.

    Returns:
        list: A list of seeds if the file exists, otherwise None.
    """
    if seeds_file.is_file():
        seeds = np.loadtxt(seeds_file, dtype=np.uintc).tolist()
        return seeds
    else:
        print(f"Seed file not found at {seeds_file}")
        return None
