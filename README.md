<div align="center">
  <img src="https://raw.githubusercontent.com/Ikomia-hub/dataset_wildreceipt/main/icons.png" alt="Algorithm icon">
  <h1 align="center">dataset_wildreceipt</h1>
</div>
<br />
<p align="center">
    <a href="https://github.com/Ikomia-hub/dataset_wildreceipt">
        <img alt="Stars" src="https://img.shields.io/github/stars/Ikomia-hub/dataset_wildreceipt">
    </a>
    <a href="https://app.ikomia.ai/hub/">
        <img alt="Website" src="https://img.shields.io/website/http/app.ikomia.ai/en.svg?down_color=red&down_message=offline&up_message=online">
    </a>
    <a href="https://github.com/Ikomia-hub/dataset_wildreceipt/blob/main/LICENSE.md">
        <img alt="GitHub" src="https://img.shields.io/github/license/Ikomia-hub/dataset_wildreceipt.svg?color=blue">
    </a>    
    <br>
    <a href="https://discord.com/invite/82Tnw9UGGc">
        <img alt="Discord community" src="https://img.shields.io/badge/Discord-white?style=social&logo=discord">
    </a> 
</p>

Load the Wildreceipt dataset format. This plugin converts a Wildreceipt dataset format to Ikomia format.

The Wildereceipt format is specifically designed for receipt OCR (Optical Character Recognition) tasks.


## :rocket: Use with Ikomia API

#### 1. Install Ikomia API

We strongly recommend using a virtual environment. If you're not sure where to start, we offer a tutorial [here](https://www.ikomia.ai/blog/a-step-by-step-guide-to-creating-virtual-environments-in-python).

```sh
pip install ikomia
```

#### 2. Create your workflow

[Change the sample image URL to fit algorithm purpose]

```python
from ikomia.dataprocess.workflow import Workflow

# Initialize the workflow
wf = Workflow()

# Add the dataset loader to load your custom data and annotations
algo = wf.add_task(name="dataset_wildreceipt", auto_connect=True)

algo.set_parameters({"dataset_folder":"path/to/dataset/folder"})

# Add the training algorithm
train = wf.add_task(name= "train_mmlab_text_recognition",  auto_connect=True)
   
# Launch your training on your data
wf.run()
```

## :sunny: Use with Ikomia Studio

Ikomia Studio offers a friendly UI with the same features as the API.

- If you haven't started using Ikomia Studio yet, download and install it from [this page](https://www.ikomia.ai/studio).

- For additional guidance on getting started with Ikomia Studio, check out [this blog post](https://www.ikomia.ai/blog/how-to-get-started-with-ikomia-studio).


## :fast_forward: Advanced usage 

 Check out the [dataset loader guide](https://www.ikomia.ai/blog/using-dataset-loaders-to-train-a-custom-model-with-the-ikomia-api#working-with-wildreceipt-dataset-format) for more information.
