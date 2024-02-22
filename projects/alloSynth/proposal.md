<h1>Proposal: Audio-Visual Spatial Harmonic Synthesizer</h1>

<h2>Basis</h2>

In the paper [*CymaSense: A Real-Time 3D Cymatics-Based Sound Visualization Tool*](https://www.researchgate.net/publication/317488460_CymaSense_A_Real-Time_3D_Cymatics-Based_Sound_Visualisation_Tool) published in 2017, the authors created a program called CymaSense to visualize the “propagation of a sound wave through a fluid in 3 dimensions.”

The shapes in the CymaSense audio-visualization tool are based on two dimensional depictions of the popular Chladni patterns, which are produced by the displacement of sand caused by the resonating of a metal plate with a bow, which is what they refer to in the paper as "quasi-3D patterns". However, beautiful as the visualizations may be, in my opinion the CymaSense visualizer does not give the viewer the sense of three dimensionality. My project will instead visualize sound waves in shapes produced in other physical demonstrations more conducive to three dimensional visualization than those done on the Chladni plates. Similarly to CymaSense, this project will implement the technique of interpolating between shapes produced by physical cymatic demonstrations to create the real-time visualization of synthesized audio. Also similarly, this project will not be a simulation using equations related to the physics of how sound travels through materials in three dimensions. The goal is to reference physical phenomena in the creation of a performative audio-visual synthesizer with cohesive and interesting interplay between the sonic and visual material.

A video here of an experiment conducted by W. Ran and S. Fredericks at Clemson University titled - [*Cymatics in 3D*](https://www.youtube.com/watch?v=5qmQynxqGjY) shows that when modulated with a single tone of a harmonic of the drops resonant frequency, the fluid oscillates in a star shape with a number of facets linearly related to the order of the harmonic. I believe the title of this video to be a misnomer and the experiment is instead another display of quasi-three-dimensional cymatics, as the video clearly shows the single transducer-reflector pair to be modulating the shape of the three dimensional droplet on only two axes. Nonetheless, the results of this experiment do serve as an effective basis from which one might be able to imagine three dimensional shapes which may result from the usage of *two or more* transducer-reflector pairs. The oscillation of the droplet's facets also serve as a strong and interesting visual cue for audio oscillators. This imagining will be the basis for our visualization.

<h2>Method</h2>

Several droning sine wave oscillators will be represented by a cluster of metaballs in a raymarched shader. Each oscillator is tuned based on the overtone of a fundamental frequency of the users choosing. The user will be able to scan through the overtones of the fundamental for the tuning of each oscillator. Based on the harmonic which is chosen, each cluster of metaballs will begin to oscillate based on the three-dimensional reimagining of *Cymatics in 3D*, at a speed corresponding to the frequency of the sine wave oscillator's tone. The metaballs will rotate in orbit around the viewer subtly affected by external forces applying velocity and repulsing them from each other. When the metaballs approach each other, their respective sine wave oscillators will frequency modulate one another. The shape of the metaball's oscillation will reflect the increase in harmonics through an analysis of the frequency material in the sound spectrum of each oscillator. The metaballs will oscillate in a way based on the combination of the amplitude of the material in each frequency bin. One could imagine the sum of each bin's corresponding oscillation looking like this representation of [3D Cymatics in High Performance Bubbles](https://www.hubmedia.ca/news-blog/research-and-development-3d-cymatics-in-high-performance-bubbles), where the fluid when affected by a sound wave with more harmonic content would take an irregular shape.

Purposed for the AlloSphere, the video and audio synthesizer will include 3D spatial audio panning and three dimensional projection. The panning of each oscillator will correspond to the position of each metaball cluster in 3D space. A subtle reverb subject to filtering for each oscillator will further emphasize the impression of the distance of objects from the viewer.

Control of the synthesizer will be from a 8 x 16 two dimensional grid. The user will navigate the grid to interpolate between different states of the positionality of the metaballs and other parameters. A variational autoencoder will be trained on different states of the synthesizer's parameters, and the grid will navigate it's latent space in two dimensions. The position of the current state in the two dimensional latent space will be reflected by a light on the grid. Other parameters will be adjustable by individual faders only, and not subject to state change.

<h2>Variable Parameters</h2>

These are variable parameters of the synthesizer, which may be subject to either state change from the variational autoencoder or direct control by the user. Each of these variables will exist individually for each cluster:

- Travel Forces:
   - Position of clusters.
   - Speed of metaballs as they rotate around viewer.
   - Weight of the repulsion force between metaballs as they approach each other.
   - Amount of randomness / chaos in forces.

- Oscillation Forces:
   - Amount of oscillation force applied to metaballs.
   - Amount of randomness / chaos in oscillation pattern.
   - Amount which the amplitude of each bin in the audio signal influences the oscillation.

- Audio:
   - Fundamental frequency.
   - Scan position between harmonic tunings.
   - Glissando rate between fundamental frequencies when changed.
   - Distance between metaballs before frequency modulation is applied.
   - Amount of frequency modulation applied.
   - Amplitude of reverb / filtering.

- State Interpolation:
   - Current state.
   - Rate of change between states from the controller.



