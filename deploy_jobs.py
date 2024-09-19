import argparse
import os
import json
import traceback

import requests
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

# Replace these variables with your information
from common import get_configs, render_template, deploy_job, get_job_template, get_job_config
# 
# DOMAIN = 'https://dbc-63695d69-a8da.cloud.databricks.com/'
# TOKEN = 'dapi25520dd420a79ec9822c37c31e08d3d5'


def process_arguments():08:34:09.440: [deployment_scripts3] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false add --ignore-errors -A -- common.py generate_entry_point_script.py test.py create_and_deploy_instance_profiles.py create_cluster_policy.py deploy_jobs.py deploy_table_assets.py
08:34:32.154: [deployment_scripts3] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false rm --ignore-unmatch --cached -r -- generate_entry_point_script.py test.py common.py create_cluster_policy.py create_and_deploy_instance_profiles.py deploy_jobs.py deploy_table_assets.py cloud_formation_templates
08:35:12.980: [deployment_scripts3] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false checkout -b Feature/init origin/dev^0 --
Switched to a new branch 'Feature/init'
08:35:22.211: [deployment_scripts3] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false add --ignore-errors -A -- deploy_table_assets.py generate_entry_point_script.py test.py common.py create_and_deploy_instance_profiles.py create_cluster_policy.py deploy_jobs.py cloud_formation_templates/online_store_dynamodb_instance_profile_cloud_formation_template.yaml
08:37:36.343: [deployment_scripts3] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false add --ignore-errors -A -f -- generate_entry_point_script.py test.py common.py create_and_deploy_instance_profiles.py create_cluster_policy.py deploy_jobs.py deploy_table_assets.py cloud_formation_templates/online_store_dynamodb_instance_profile_cloud_formation_template.yaml
08:37:36.531: [deployment_scripts3] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false commit -F C:\Users\HP\AppData\Local\Temp\git-commit-msg-.txt --
[Feature/init ce0e012] commit
 8 files changed, 680 insertions(+)
 create mode 100644 cloud_formation_templates/online_store_dynamodb_instance_profile_cloud_formation_template.yaml
 create mode 100644 common.py
 create mode 100644 create_and_deploy_instance_profiles.py
 create mode 100644 create_cluster_policy.py
 create mode 100644 deploy_jobs.py
 create mode 100644 deploy_table_assets.py
 create mode 100644 generate_entry_point_script.py
 create mode 100644 test.py
08:38:17.499: [deployment_scripts3] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false push --progress --porcelain origin refs/heads/Feature/init:refs/heads/Feature/init --set-upstream
Enumerating objects: 12, done.
Counting objects:   8% (1/12)
Counting objects:  16% (2/12)
Counting objects:  25% (3/12)
Counting objects:  33% (4/12)
Counting objects:  41% (5/12)
Counting objects:  50% (6/12)
Counting objects:  58% (7/12)
Counting objects:  66% (8/12)
Counting objects:  75% (9/12)
Counting objects:  83% (10/12)
Counting objects:  91% (11/12)
Counting objects: 100% (12/12)
Counting objects: 100% (12/12), done.
Delta compression using up to 4 threads
Compressing objects:   9% (1/11)
Compressing objects:  18% (2/11)
Compressing objects:  27% (3/11)
Compressing objects:  36% (4/11)
Compressing objects:  45% (5/11)
Compressing objects:  54% (6/11)
Compressing objects:  63% (7/11)
Compressing objects:  72% (8/11)
Compressing objects:  81% (9/11)
Compressing objects:  90% (10/11)
Compressing objects: 100% (11/11)
Compressing objects: 100% (11/11), done.
Writing objects:   9% (1/11)
Writing objects:  18% (2/11)
Writing objects:  27% (3/11)
Writing objects:  36% (4/11)
Writing objects:  45% (5/11)
Writing objects:  54% (6/11)
Writing objects:  63% (7/11)
Writing objects:  81% (9/11)
Writing objects:  90% (10/11)
Writing objects: 100% (11/11)
Writing objects: 100% (11/11), 7.37 KiB | 754.00 KiB/s, done.
Total 11 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas:   0% (0/2)        
remote: Resolving deltas:  50% (1/2)        
remote: Resolving deltas: 100% (2/2)        
remote: Resolving deltas: 100% (2/2), done.        
remote: error: GH013: Repository rule violations found for refs/heads/Feature/init.        
remote: 
remote: - GITHUB PUSH PROTECTION        
remote:   —————————————————————————————————————————        
remote:     Resolve the following violations before pushing again        
remote: 
remote:     - Push cannot contain secrets        
remote: 
remote:             
remote:      (?) Learn how to resolve a blocked push        
remote:      https://docs.github.com/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line#resolving-a-blocked-push        
remote:             
remote:             
remote:       —— Databricks Access Token ———————————————————————————        
remote:        locations:        
remote:          - commit: ce0e012b73c5d5dd00c3bac06110c3f445e0e9fe        
remote:            path: deploy_table_assets.py:13        
remote:             
remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.        
remote:        https://github.com/Sindhujajuttuu/deployment_scripts/security/secret-scanning/unblock-secret/2mGugdNblyZhnGzFz3muOKOmCip        
remote:             
remote:             
remote:       —— Databricks Access Token ———————————————————————————        
remote:        locations:        
remote:          - commit: ce0e012b73c5d5dd00c3bac06110c3f445e0e9fe        
remote:            path: deploy_jobs.py:13        
remote:             
remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.        
remote:        https://github.com/Sindhujajuttuu/deployment_scripts/security/secret-scanning/unblock-secret/2mGugkEmSHp3YyTKbiNWjb0oHX4        
remote:             
remote: 
remote: 
error: failed to push some refs to 'https://github.com/Sindhujajuttuu/deployment_scripts.git'
To https://github.com/Sindhujajuttuu/deployment_scripts.git
!	refs/heads/Feature/init:refs/heads/Feature/init	[remote rejected] (push declined due to repository rule violations)
Done

    parser = argparse.ArgumentParser(
        description=(
            "Used to deploy  jobs to databricks. It takes two arguments --templates_path: path where job jinja "
            "template exists --template_name name of the template to process"
        )
    )

    parser.add_argument("--templates_path", type=str, required=True, help="template path")
    parser.add_argument("--template_name", type=str, required=True, help="template name")
    parser.add_argument("--config_path", type=str, required=True, help="config path")

    return parser.parse_args()


try:
    args = process_arguments()

    # Define the path to the directory containing the template
    template_dir = args.templates_path  # Directory path containing the template file
    template_file = args.template_name  # Template file name
    config_path = args.config_path

    # Check if the template directory exists
    template = get_job_template(template_dir, template_file)

    template_vars = get_configs(config_path)
    # Render the Jinja template with the configuration variables
    job_config = render_template(template_vars, template)
    print(job_config)
    # Convert the rendered JSON template to a dictionary
    job_config_dict = get_job_config(job_config)

    print(job_config_dict)
    deploy_job(job_config_dict, DOMAIN, TOKEN)

except Exception as e:
    print(traceback.format_exc())
    raise e
