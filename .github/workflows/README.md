# Building SLiCAP Documentation

## Creating A workflow

Workflows are created after the keyword "on". In this yaml file I create:

1. workflow which is triggered from the SLiCAP_python repository. 

### SLiCAP Triggered Workflow

This workflow is triggered from the SLiCAP_python repository. When a 'Push' is made in the SLiCAP_python repository a [Repository Webhook](https://docs.github.com/en/free-pro-team@latest/rest/repos/webhooks?apiVersion=2022-11-28#create-a-repository-webhook) request is made with the tag "Trigger_Workflow" and sent to this repository.

## Jobs

The jobs that need to be completed are

1. Install Wine, LTspice 

3. Install python and SLiCAP

4. Run Tests

5. Setup pages

6. upload artifact
