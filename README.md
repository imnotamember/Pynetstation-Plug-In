[![DOI](https://zenodo.org/badge/30547356.svg)](https://zenodo.org/badge/latestdoi/30547356)

# Pynetstation-Plug-In
Plug-in for OpenSesame to use EGI's Netstation EEG software

This plug-in includes 8 items:
- pynetstation source files (in folder egi)
——These files are almost identical to the ones available at
https://code.google.com/p/pynetstation/ except a correction in the
padding function and editing of the fake.py to make better use of a
fake Netstation connection in the OpenSesame environment
- pynetstation initializer
——This should be used once in any experiment(will throw an error if
used more than that) if you want to create multiple Netstation
recordings in a single experiment use the pynetstation reinit item
after you end any sessions in your experiment. Really cool: set your
threading to Faker! and you can try out your experiment and get
feedback without actually being connected to Netstation, really useful
if you are like me and don’t have an EGI set up at home to work with
and would rather not live in your lab space.
- pynetstation start recording
——Pretty straight forward, presses record in Netstation
- pynetstation pause recording
——Pretty straight forward, presses pause in Netstation
- pynetstation begin trials
——This tells Netstation to synchronize its clock with Opensesame, which
is crucial during experiments as the clock drifts over time. Make sure
this is within the loop you want to record events from.
- pynetstation send tags
——Sends Netstation events from OpenSesame, fill in the blanks with your
information for your event.
- pynetstation end
——Pretty straight forward, saves and closes the Netstation session
- pynetstation re-initializer
——Use this after you use ‘pynetstation end’ in your experiment to
reconnect to Netstation. Just make sure you open a new recording
session in Netstation before running this, or you’ll crash the
experiment.
