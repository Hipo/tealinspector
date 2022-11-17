# tealinspector

## Install the dependency

```python
pip install tealinspector
```

## Use in CLI

```python
tealinspector --network mainnet --application_id 942781578 --program_counter 1328
```

Additionally, You can pass `--line_count` parameter. The default value is `25`.

### Output

```python
Line: 594
574 == 
575 && 
576 gtxn 4 NumAppArgs 
577 intc_0 // 1 
578 == 
579 && 
580 gtxna 4 Assets 0 
581 bytec_2 // "global_list_asset" 
582 app_global_get 
583 == 
584 && 
585 gtxna 4 Accounts 1 
586 bytec_1 // "global_list_owner" 
587 app_global_get 
588 == 
589 && 
590 gtxna 4 Accounts 2 
591 bytec 8 // addr KQMEN76UOQEHGXPBXUMRGW3KFI7Z57IFXBXWO77HAXYKMISCZF5CAOOITI 
592 == 
593 && 
594 assert <---------- 
```

## About

Developed by [Hipo](https://hipolabs.com).
Licensed under MIT.
