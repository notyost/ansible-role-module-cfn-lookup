#!/usr/bin/env python

import collections
from ansible import utils, errors
import json
import sys
from ansible.module_utils.basic import *

try:
  import boto3
except ImportError:
  raise errors.AnsibleError(
    "Can't LOOKUP(cloudformation): module boto3 is not installed")

def main():
  module = AnsibleModule(
    argument_spec = dict(
      stack_name = dict(required=True, type='str')
    )
  )

  stack_name = module.params.get('stack_name')
  region = module.params.get('region')

  cfn_client = boto3.client('cloudformation')

  outputs_fixed = {}
  stacks = cfn_client.describe_stacks(StackName=stack_name)['Stacks']

  if len(stacks) == 0:
    module.exit_json(
      Changed=False,
      Failed=True,
      msg=('Stack: {0} was not found!'.format(stack_name))
    )

  for output in stacks[0]['Outputs']:
    outputs_fixed[output['OutputKey']] = output['OutputValue']

  module.exit_json(
    Changed=False,
    Failed=False,
    Outputs=outputs_fixed
  )

main()
