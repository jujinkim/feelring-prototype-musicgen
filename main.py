import sys
import musicgenerator

def main():
    # Get command line arguments
    args = sys.argv[1:]

    # If args is empty string or null then print "No prompt" and return 1
    if args == None or args == [] or args == [''] or args == "":
        print("No prompt, please provide a prompt to generate music.")
        return 1
    
    # If args is not empty string then print "Prompt: " and the args, and Generate music and write to file
    print("Prompt: ", args)
    print("Generating music and writing to file")
    generator = musicgenerator.MusicGenerator(musicgenerator.MusicGenModel.SMALL, 30)
    wave = generator.generate(args)
    generator.writeAudio(wave, "output.wav")
    print("Music generated and written to file")
    return 0

if __name__ == "__main__":
    main()