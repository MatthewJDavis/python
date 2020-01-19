# system-info

Basic python program to return system information.

## Python version
Written for Python3

## Concourse CI

ci directory holds a Concourse pipeline that can be used to run the program.
Proof of concept of how to use Concourse for python programs.
Task is abstracted out to the tasks directory.

To create the pipeline:

```bash
fly -t ps set-pipeline -p python-system-info -c ci/pipeline.yml
```
