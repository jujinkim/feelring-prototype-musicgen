# Feelring prototype: using musicgen

This is a music-generation-by-ai backend prototype, using Meta MusicGen Generative-AI model.

## Setup at Windows

1. Clone the repository.
2. Create `conda` virtual env and activate it.
3. Install dependency packages refer to `requirements.txt`.

    ```Powershell
    pip install -r requirements.txt
    ```

4. You may need to install Microsoft Visual C++ 14 or above build tool.
    > Go to [Microsoft C++ Build Tools Download page](https://visualstudio.microsoft.com/visual-cpp-build-tools/),  
    > Install C++ Build Tool (`Desktop development with C++`)
5. You may need to turn off your vaccine app's realtime detection feature.
6. Run `main.py` with the prompt to generate music.

    ```Powershell
     python main.py "Happy rock song"
    ```

7. Wait until the complete message is printed.
    > Message: `Music generated and written to file`
8. Check `output.wav` file.
