Widget for PyQt5 that aims to display any kind of keyboard.

Supported keyboards:
* Spanish QWERTY
* any other as long as you are willing to follow the following steps

# How to add your own layout
See `layouts/QWERTY_es.keyb` for reference.

1. Create a .keyb file in the `layouts` folder
2. Write the labels of each key separated by `##`. Trailing and leading whitespace is ignored.
3. Separate the sections of the keyboard with `---#---`

The sections are:

1. Core of the keyboard. Example:
    ```
    ESC        ##F1 ##F2 ##F3##F4##F5##F6##F7##F8##F9##F10##F11##F12   
    º          ##1  ##2  ##3 ##4 ##5 ##6 ##7 ##8 ##9 ##0  ##'  ##¡     ##<-
    TAB        ##Q  ##W  ##E ##R ##T ##Y ##U ##I ##O ##P  ##`  ##+     ##ENTER
    BLOQ\nMAYÚS##A  ##S  ##D ##F ##G ##H ##J ##K ##L ##Ñ  ##´  ##Ç     ##ENTER
    LMAYÚS     ##<  ##Z  ##X ##C ##V ##B ##N ##M ##, ##.  ##-  ##RMAYÚS
    LCONTROL   ##WIN##ALT##                       ##ALT GR##FN##MENU##RCONTROL
    ```
2. Navigation keys (the ones between the core and the numpad). Example:
    ```
    IMPR\nPANT##BLOQ\nDESPL##PAUSA\nINTER
    INSERT    ##INICIO     ##RE\nPÁG
    SUPR      ##FIN        ##AV\nPÁG
    ```
3. Arrow keys. Example:
    ```
    ᐃ
    ᐊ##ᐁ##ᐅ
    ```
4. Numpad
    
    The long keys of the numpad must only be written in the last line, in this order: top right, bottom right, top left. Example:
    ```
    BLOQ\nNUM##/##*##-
        7##8##9##+
        4##5##6
        1##2##3
              ,
    +##INTRO##0
    ```
5. The length of certain keys. Any key not mentioned will have a length of 1. Example:
    ```
             <-: 2
            TAB: 1.5
    BLOQ\nMAYÚS: 1.75
         LMAYÚS: 1.25
         RMAYÚS: 2.75
       LCONTROL: 1.5
            ALT: 1.25
               : 6.5
         ALT GR: 1.25
       RCONTROL: 1.5
  ```
