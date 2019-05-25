# Design Docs
## Hardware
* Pi 3
    * I/O pins
        * Screen
        * 
    * (Audio output)
* 4 Way directional pad (some options)
    * https://www.sparkfun.com/products/9426
        * Slider Joystick
    * https://www.sparkfun.com/products/9032
        * Conventional joystick with centre click
        * This and the above would allow for wider range of movement
    * https://www.amazon.com/NOYITO-Tactile-Breakout-Development-Transfer/dp/B07G4266RP
        * "5-way switch"; 4 direction buttons plus centre click
        * Would need some sort of hat (GBA-style)
* 4 buttons 
* Screen
    * HyperPixel 4
        * https://shop.pimoroni.com/products/hyperpixel-4?gclid=Cj0KCQjwoInnBRDDARIsANBVyAQEdCFbW2MIgH_4ws63d-Oqjsrdy8giGblh06uy5Y8JUMPQF_DIk3saAj4wEALw_wcB&utm_campaign=google%20shopping&utm_medium=cpc&utm_source=google&variant=12569539706963 ?
        * 800 x 480
        * 86.4 x 51.8mm
        * 18-bit colour

## Game Specs
**Must Have**
* Must be able to run on a raspberry pi 
    * Python, C, C++, Java, Scratch, Ruby, HTML5, Javascript & JQuary, Perl, Erlang
* Resolution between 800 x 480 (or smaller and has black bars)
* Must have metadata file
    * Must have a name
* The file that is run must be called Main.py 

**Optional**
* Metadata file can contain other information
    * Topright screen left to author (ideas listed below)
        * Big logo
        * Video/Gif of game playing 
            * Avoid massive video files 
        * Big logo


## MetaData File Structure
* Must be in the same location as the game
* Called MetaData.yaml
* File structure
    * First Line is name of the game:
    * Name: "Name of the game"
    * Logo: Path to logo (Optional)
    * Animation: Path to gif/video (Optional)
    * Info: Information about the game displayed on the bottom of the screen (Optional)
    * If none of the optionals are supplied then "no infomation supplied" is displayed on screen 

## To do list 
* Pixel pineapple
* Make example MetaData.yaml
* Games/etc ideas testing
    * Pong
    * Cool Screensaver
* Menu demo
* Finding out how to draw to the screen
* Finding/making a nice font