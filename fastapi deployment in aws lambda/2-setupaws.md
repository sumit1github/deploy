
# creating aws user 

> go to aws IAM management

> create user
* assign permission policies
    * AmazonEC2ContainerRegistryFullAccess
    * AWSLambda_FullAccess
* download the csv contains `Access key` and `secret key` and `region`


# aws CLI install
>go to this page

* https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html

> search
* For the latest version of the AWS CLI


# create a AWS ECR (Elastic Container Registry)

* create reposisitory
* private
* give a name
* create

>`From the list select the repo`

* view push commands (at the top right)
* follow the commands

>`view push commands`

>run below command to se where the aws cli is installed and copy the `aws_cli_path`
>> which aws

> to very aws cli is working
>>`aws_cli_path` --version

> configure the aws cli
>>`aws_cli_path` configure

* enter as input the `Access key` and `secret key` and `region` and `json`

> go to the folder where your dockerfile is present
* now run the docker build command from the instructions
* and push this



# process to push code 2 time onwards
>> docker build -t <new_build_name> .

>> sudo docker tag `new_build_name`:latest 865049059586.dkr.ecr.eu-north-1.amazonaws.com/starterkit-ml:latest

* use the push command written on the aws ecr instruction
* follow this step below -> `Now select the lambda Image from the list`


# Create a AWS Lambda

> Create function

> container image

> function name

> Browse images

* select repository
* select image

> Architecture
* select `x86_64`

> Change default execution role
* Create a new role with basic Lambda permissions

> `Now select the lambda Image from the list`
* Select `Image` --> from (image, test, monitor, configurationaliases, Versions)
    * click on `Deploy new image` button on top-right
        * Browse images
            * click repository dropdown and select repo
                * select the new image with `latest` tag and click on `select image` bottom right.


> Select `configuration` --> from (image, test, monitor, configuration, aliases, Versions)
* select `Function URL` from left menu
    * Auth type --> None
    * Additional settings --> BUFFERED (default)
    * Configure cross-origin resource sharing (CORS) --> Check
    * Allow origin --> *

> Now use the function Url