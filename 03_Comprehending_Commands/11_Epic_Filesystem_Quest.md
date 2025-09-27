# An Epic Filesystem Quest

Find the flag hidden behind multiple directories

## My solve
**Flag** `pwn.college{Q_777Ry_5tcbYYdVlJJgUhdodLp.QX5IDO0wCO2gjNzEzW}`

```
cd /
ls
cat ALERT
cd /usr/local/lib/python3.8/dist-packages/jupyter_server/files/__pycache__
ls
cat CUE
cd /usr/lib/python3/dist-packages/zope/interface/common/tests/__pycache__
ls
cat TEASER
cd /usr/lib/python3/dist-packages/python3_openid-3.1.0.egg-info
ls
cat NUGGET
cd /usr/share/javascript/mathjax/unpacked/jax/output/SVG/fonts/TeX/Main/Bold
ls
cat EVIDENCE
cd /usr/share/glib-2.0/schemas
cat TRACE
cd /opt/linux/linux-5.4/tools/testing/selftests/powerpc/eeh
ls -a
cat .POINTER
cd /usr/local/lib/python3.8/dist-packages/jedi/third_party/django-stubs/django-stubs/contrib/contenttypes/management/commands
ls
cat SPOILER
cd /opt/tcpdump/.git/refs/heads
ls
cat MESSAGE-TRAPPED
```

## What I learned
Hints and the flag can be trapped in a serious of files and we need to find the clues leading up to the flag
