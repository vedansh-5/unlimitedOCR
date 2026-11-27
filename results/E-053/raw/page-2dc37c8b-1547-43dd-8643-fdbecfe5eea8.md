<|det|>text [139, 48, 856, 660]<|/det|>#没有定义
[root@ubuntu ~]# ansible-playbook when-1.yaml

PLAY [localhost]
**************************
** *
TASK [debug]
**************************
*****
ok: [localhost] => {
    "msg": "undefined"
}

PLAY RECAP
**************************
**************************
localhost : ok=1 changed=0 unreachable=0 failed=0 skipped=0
rescued=0 ignored=0

#定义
[root@ubuntu ~]# ansible-playbook -e tom=cat when-1.yaml

PLAY [localhost]
**************************
** *
TASK [debug]
**************************
skipping: [localhost]

PLAY RECAP
**************************
localhost : ok=0 changed=0 unreachable=0 failed=0 skipped=1
rescued=0 ignored=0
<|det|>text [124, 761, 244, 777]<|/det|>范例：循环判断
<|det|>text [139, 797, 437, 927]<|/det|>[root@ubuntu ~]# cat when-11.yaml
--- #when-11
- hosts: localhost
gather_facts: no
tasks:
- debug: msg={{ item }}
    with_items: [1,2,3,4,5]
    when: item > 3
