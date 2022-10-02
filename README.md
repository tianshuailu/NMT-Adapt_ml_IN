# Applying NMT-Adapt to Malayalam

Install sentencepiece and fairseq
```
pip install sentencepiece

git clone -b v0.10.2 https://github.com/facebookresearch/fairseq.git
cd fairseq
pip install --editable ./
```
We used fairseq `v0.10.2` since we encountered compatible issues with the new fairseq release.

The training steps are from this GitHub repository https://github.com/wjko2/NMT-Adapt

## Running the experiment
### Transliteration
Before running the experiment, use the following python code to transliterate the Malayalam script into the Devanagari script.
```
./scripts/Transliteration.py
```
### Pretraining mBART
Start with finetuning a [mBART](https://github.com/facebookresearch/fairseq/tree/main/examples/mbart) model. The commands are described in:
```
./Pretrain_mBART.ipynb
```
### Back-translation
Next, use the pretrained [mBART](https://github.com/facebookresearch/fairseq/tree/main/examples/mbart) model to generate English Malayalam back-translation pairs. The commands are described in:
```
./Back_translation.ipynb
```
### Preprocessing the data
Next, follow the commands below to preprocess the datasets, including the test dataset.
```
./Preprocess_data.ipynb
```
### Training
Before training the model, download and open this directory:
```
./NMTAdapt_ml
```
then install the adapted version of fairseq with
```
pip install --editable ./
```
Next, follow the commands from this file to train the model:
```
./NMTAdapt.ipynb
```
The evaluation command is also included.

All additional python code we used during the experiment are in this directory:
```
./scripts
```

## Language data
The Malayalam monolingual data are from https://ai4bharat.iitm.ac.in/corpora

The English Hindi parallel data are from https://ai4bharat.iitm.ac.in/samanantar

