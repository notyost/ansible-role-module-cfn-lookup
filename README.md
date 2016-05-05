# ansible-role-module-cfn-lookup
Role / Module for looking up CloudFormation outputs

This can be used as either a role or a module. 

If used as a role, run the role with the <strong>cfn_lookup_stack_name</strong> parameter:
```
roles:
  - role: cfn_lookup
    cfn_lookup_stack_name: "some_stack"
```
Then you can retrieve the stack outputs from the stack_outputs fact:
```
tasks:
  - debug: var=stack_outputs
```
<em>Note: The actual outputs will be nested differently within the stack_outputs fact depending on whether you're using ansible 1 or 2. If 1, the outputs will be <strong>stack_outputs.Outputs</strong>. If 2, you will find them in <strong>stack_outputs.results[0].Outputs</strong></em>    

If module, just run the role first with no parameters, then run the module as a task:
```
- name: Look up stack outputs by stack name
  cfn_lookup: 
    stack_name: "some_stack"
  register: stack_outputs 
```
