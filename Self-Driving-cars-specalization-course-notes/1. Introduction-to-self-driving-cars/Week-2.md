## Week 2

What will Learn:

1. sensors for preception
2. hardware
3. software architecture, decomposition
4. Desigining hardware configuration
5. environment representation

### 1. Sensors
They are catego into two extro(external) and Proprio(internal)

1. Camera (extro):

    Comparision matrix:

        1. Resolution
        2. Field of view
        3. Dynamic range

    Tradeoff between Resolution and Field of view

        As FOV increases we need to increase the resolution to get much more accurate information from the image

2. LIDAR (Light detection and Ranging sensor)(extro):

    Detailed 3D scene gemotery from LIDAR point cloud

    Comparision matrix:

        1. Number of beams (8, 16, 32, 64)
        2. Points per second (more the points, more accurate the LIDAR is)
        3. Rotation Range (more rotation better)
        4. Field of view

    **Solid state LIDAR**

3. RADAR (Radio detection and ranging)(extro):

    Robust object detection and Relative speed estimation

    Comparision Matrix:

        1. Range
        2. Field of view
        3. position and speed accuracy

    Configurations:

        1. WFOV - Wide field of view, (short range)
        2. NFOV - Narrow field of view, (longe range)
        
4. Sonors (extro):

    - Short range all-weather distance mesaurment
    - Ideal for low cost parking solution
    - uneffected ny lightinig and precipitation
    
    Comparision matrix:

        1. Range
        2. FOV
        3. Cost
    
5. GNSS/IMU (Global navigation satellite system / Intertial measurment unit) (proprio)

    - Direct measure of ego vehicle state
    - they can get us position of vehicle and velocity of the vehicle (varying accuries : RTK, PPP, DGPS)
    - angular rotation rate (IMU)
    - acceleration (IMU)
    - heading (IMU, GPS)


### 2. hardware

- GPUs 
- FPAGAs - Field programmable gate array
- ASICs - Application specific integrated chip
