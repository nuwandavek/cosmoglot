docker run -d --gpus '"device=0,5,6,7"' \
    -v /home/gcpnode2/bayesian_conspiracy/ollama_stuff:/root/.ollama \
    -v /home/gcpnode2/bayesian_conspiracy/data:/root/data \
    -p 11434:11434 \
    -e OLLAMA_NUM_PARALLEL=4 \
    --name ollama \
    ollama/ollama
