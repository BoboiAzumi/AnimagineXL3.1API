from gradio_client import Client

client = Client("cagliostrolab/animagine-xl-3.1")

def animagine(
                prompt,
                neg_prompt,
                seeds,
                width,
                height,
                scale,
                steps,
                sampler,
                ratio,
                style,
                quality,
                upscaler,
                strength,
                upscale,
                quality_tags
            ):
    
    result = client.predict(
		    prompt,
    		neg_prompt,
	    	seeds,
		    width,
		    height,
		    scale,
		    steps,
		    sampler,
		    ratio,
		    style,
		    quality,
		    upscaler,
		    strength,
		    upscale,
		    quality_tags,
		    api_name="/run"
        )
    
    return result