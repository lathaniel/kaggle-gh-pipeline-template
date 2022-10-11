import os
import json

def main():
    if not os.path.exists('.kaggleconfig'):
        raise Exception(
            'Must supply a .kaggleconfig file in the root directory'
        )
    
    with open('.kaggleconfig', 'r') as f:
        # Read in kaggle config file
        data = json.loads(f.read())

        os.makedirs(
            data["kaggle-data-directory"],
            exist_ok=True
        )

        # Write the dataset-metadata file
        with open(
            data["kaggle-data-directory"] + '/dataset-metadata.json',
            'w+'
        ) as w:
            w.write(json.dumps(data["dataset-metadata"], indent=4))
        
        # Write the dataset-metadata file
        with open('./kernel-metadata.json', 'w+') as w:
            w.write(json.dumps(data["kernel-metadata"], indent=4))


if __name__=="__main__":
    main()