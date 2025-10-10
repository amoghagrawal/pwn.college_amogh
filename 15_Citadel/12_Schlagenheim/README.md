# DESCRIPTION
Repair the corrupted file to reveal the flag

# WRITEUP

- The title and the slight hints in the description suggest that the corrupt file is a **MIDI** file
- Just opening the .wav file doesnt work
- Using HxD we can see the first four hex values corresponding to MIDI again suggesting at a MIDI file
- Searched on google for the file formats and got **.mid**
- The .mid file didnt give anything in itself because the hex said MIDI instead of MThd
- Changing the hex from `4D 31 44 31` to `4D 54 68 64` we get the desired MThd
- After fixing the header, the file could now be opened properly as a **MIDI** file
- Tried converting the MIDI to .txt file but that was a deadend
- Also converted the MIDI to a .csv file
- Each MIDI event has a **delta time** property that indicates how long to wait since the previous event
- By summing these delta times, we can get the absolute time for each note
- Every event also has a status byte that tells what kind of message it is
- When the status byte indicates a Note On event, the next two bytes represent:
  - Note number (which note is being played)
  - Velocity (how hard the note is played)
- By iterating through the events and keeping a **running total of time**, we can reconstruct the sequence of notes as **pairs of (time, note number)**
- Exported the notes to a CSV to visualize and analyze the pattern
- Using the note sequences, we could finally decode the message to get the flag

> citadel{8lackM1D1wa5c00l}