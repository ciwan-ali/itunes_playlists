import plistlib

def findDuplicates(fileName):
    print("Finding duplicare tracks in %s.." %fileName)

    # Read in a playlist
    plist = plistlib.readPlist(fileName)
    # Get the tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # Create a track name dictionary
    trackNames = {}
    # Iterate through the tracks
    for trackId, track in tracks.items():
        try:
            name = track["Name"]
            duration = track["Total Time"]
            # Look for existing entries
            if name in trackNames:
                if duration // 1000 == trackNames[name][0] // 1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count + 1)
                else:
                    trackNames[name] = (duration, 1)
        except:
            pass
