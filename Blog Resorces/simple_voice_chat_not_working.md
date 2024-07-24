
# Simple Voice Chat Mod Not Working?

## What is Simple Voice Chat?
The Simple Voice Chat mod is a proximity voice chat mod for Minecraft that enables players to communicate with each other using their microphones within the game environment. Here are the key aspects and features of the mod:

### Key Features:
1. **Proximity Voice Chat**: Allows players to hear each other when they are within a certain distance.
2. **Push to Talk and Voice Activation**: Players can choose between push-to-talk or voice activation for their microphones.
3. **Group Chats**: Enables players to communicate with others outside their immediate vicinity by creating or joining group chats.
4. **Password Protected Group Chats**: Offers secure group communication by setting passwords.
5. **Microphone and Audio Settings**: Includes options for microphone testing, amplification, individual player volume adjustment, and configuring the push-to-talk key.
6. **Noise Suppression and Quality**: Utilizes RNNoise for noise suppression and the Opus codec for high-quality audio.
7. **3D Sound**: Provides a spatial audio experience, making it sound as if the voice is coming from a specific direction.
8. **Cross Compatibility**: Works across various Minecraft server types and mods including Fabric, NeoForge, Forge, Quilt, Bukkit, Spigot, Paper, Velocity, BungeeCord, and Waterfall.
9. **API and Addons**: Features a robust API for developers to create additional functionalities and a variety of available add-ons.
10. **Encryption and Security**: Voice communication is encrypted, although users are advised to use it at their own risk regarding security guarantees.
11. **Recording**: Allows audio recording with separate audio tracks.
12. **User Interface**: Accessible via the V key, the GUI allows users to configure settings, manage group chats, mute themselves, and more.

### Setup and Configuration:
- **Server Setup**: Requires a specific server setup, including opening port 24454 UDP by default (configurable).
- **Settings Menu**: Accessible via the V key, where players can adjust volume, microphone amplification, recording/playback devices, and enable microphone testing.

### Important Notes:
- **Port Configuration**: The server port (24454 UDP by default) must be open for the voice chat to function.
- **Security**: While the voice chat is encrypted, absolute security is not guaranteed.

This mod enhances the multiplayer experience in Minecraft by providing a robust and configurable voice communication system, making in-game interactions more immersive and realistic.
##  Problems Fixes
### Ports Closed
#### Solve Using 'iptables'
Write terminal these commands in the same order.

    sudo iptables -A INPUT -p tcp --dport 24454 -j ACCEPT
    sudo iptables -A INPUT -p udp --dport 24454 -j ACCEPT
    sudo service iptables save

These will open the ports that simple voice chat uses for public access. Allowing players to connect via voice chat.

### Ports Access Is Blocked By Router

1. Acces Router Admin Panel
	-   Open a web browser and type your router's IP address into the address bar (usually something like `192.168.1.1` or `192.168.0.1`). Press Enter.
	-   Log in with your router’s username and password (default credentials are often found on the router or in its manual).
2. Locate the Port Forwarding Section
	- Navigate to the `Port Forwarding`, `Applications & Gaming`, or similar sections of the router's settings.
3. Create a New Port Forwarding Rule For Voice Chat
	- Click on `Add New` or `Create Rule` depending on your router’s interface.
	- Write the server's local IP at `IP ADDRESS`.
	- Write `24454` at `PORT`.
	- Set `Protocol` to `UDP` =>If set to `BOTH` server may run Minecraft at this port too.
4. Create a New Port Forwarding Rule For Minecraft Server
	- Click on `Add New` or `Create Rule` depending on your router’s interface.
	- Write the server's local IP at `IP ADDRESS`.
	- Write `25565` or any other wanted port at `PORT`.
	- Set `Protocol` to `TCP` or `BOTH` 
5. Save The Settings And Make Sure It's Enabled

### All Ports Are Running Minecraft Server 
1. Acces Router Admin Panel
	-   Open a web browser and type your router's IP address into the address bar (usually something like `192.168.1.1` or `192.168.0.1`). Press Enter.
	-   Log in with your router’s username and password (default credentials are often found on the router or in its manual).
2. Locate the Port Forwarding Section
	- Navigate to the `Port Forwarding`, `Applications & Gaming`, or similar sections of the router's settings.
3. Locate the Port Forwarding Rule For Voice Chat
	- Click on the port forwarding rule for voice chat.
	- Change `PORT` to `24454` .
	- Set `Protocol` to `UDP` =>If set to `BOTH` it's probably the reason this happened
4. Create a New Port Forwarding Rule For Minecraft Server
	- Click on `Add New` or `Create Rule` depending on your router’s interface.
	- Change`PORT` to `25565` or any other wanted port at .
	- Set `Protocol` to `TCP` or `BOTH` => TCP recommended.
5. Save The Settings And Make Sure It's Enabled
