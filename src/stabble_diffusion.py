import torch
from diffusers import StableDiffusionPipeline




class DiffModel(object):

    def __init__(self, device='cuda', model_id='CompVis/stable-diffusion-v1-4'):
        '''
        device -> options: 'cuda', 'cpu'
        '''
        self.device = device
        self.model_id = model_id
        self.pipe = self.get_pipe()



    def get_pipe(self):

        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16, requires_safety_checker=False, safety_checker=None)
        pipe = pipe.to(self.device)

        return pipe




    def generate_image(self, prompt):
        image = self.pipe(prompt).images[0]  
        return image