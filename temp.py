# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import mne
fname ="oddball_example_small-fif.gz"
raw = mne.io.read_raw_fif(fname)
raw = mne.io.read_raw_fif(fname,preload=True)
raw.plot_psd();
raw.plot();
#%%data in 20 different ica components
ica = mne.preprocessing.ICA(n_components=20, random_state=0)
#%%
ica.fit(raw.copy().filter(12,35))
#%%
ica.plot_components(outlines="skirt");
#%%we store bad components in ica object
ica.exclude=[10,13,15,16,17,18]
#%%we could also use one of the automatic algorithms
bad_idx,scores = ica.find_bads_eog(raw,"SO2",threshold=1.5)
print(bad_idx)
#%%
ica.exclude=bad_idx
#%%
raw.plot();
#%%
raw=ica.apply(raw.copy(),exclude=ica.exclude)

ica.apply(raw.copy(),exclude=ica.exclude).plot();
#%%for epoching the data we need event markers
events= mne.find_events(raw)
#%%
events
#%%
mne.viz.plot_events(events[:100]);
#%%create event ids
event_ids= {"standard/stimulus":200,
            "target/stimulus":100}
#%%epochs
epochs=mne.Epochs(raw,events,event_id=event_ids)
#%%
epochs.plot();
#%%

#%%
epochs=mne.Epochs(raw,events,event_id=event_ids,preload=True)
epochs= ica.apply(epochs, exclude=ica.exclude)
#%%baseline
epochs.apply_baseline((None,0))
#%%
epochs["target"]




 

