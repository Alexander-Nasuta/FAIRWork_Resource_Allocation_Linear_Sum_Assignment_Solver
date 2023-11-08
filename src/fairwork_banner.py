FAIRWORK_BLUE = '\033[38;2;77;155;183m'
FAIRWORK_PINK = '\033[38;2;227;155;186m'
FAIRWORK_GREEN = '\033[38;2;93;193;180m'

B = f'\033[48;2;77;155;183m{FAIRWORK_BLUE}'
G = f'\033[48;2;93;193;180m{FAIRWORK_GREEN}'
P = FAIRWORK_PINK
PBG = f'\033[48;2;227;155;186m{FAIRWORK_PINK}'

CIMA_WHITE = '\033[38;2;255;255;255m'
CIMA_WHITE_BG = '\033[48;2;255;255;255m'
W = '\033[38;2;255;255;255m'

CEND = '\33[0m'
Z = CEND

CEND = '\33[0m'
CBOLD = '\33[1m'
CITALIC = '\33[3m'
CURL = '\33[4m'
CBLINK = '\33[5m'
CBLINK2 = '\33[6m'
CSELECTED = '\33[7m'

banner_sw = f"""
                                                                                    
                                                                                    
    ████████  ██████   ██████  ███████   ██       ██                      ██        
    ██       ██    ██    ██    ██    ██  ██   █   ██                      ██        
    ██       ██    ██    ██    ██    ██  ██  ███  ██   ██████    ██████   ██    ██  
    █████    ████████    ██    ███████   ██ ██ ██ ██  ██    ██  ██    ██  ██   ██  
    ██       ██    ██    ██    ██    ██  ████   ████  ██    ██  ██        ██████    
    ██       ██    ██    ██    ██    ██  ███     ███  ██    ██  ██        ██   ██   
    ██       ██    ██  ██████  ██    ██  ██       ██   ██████   ██        ██    ██  
                                                                                
    Bringing human, AI, data and robots together.                                                                                 
"""

banner_color = f"""{P}
     ╭──────────────────────────────────╮ ╭───────────────────────────────────────────────╮
     │ https://www.fairwork-project.eu/ │ │ {CBOLD}Bringing human, AI, data and robots together.{CEND}{P} │
     ╰──────────────────────────────────╯ ╰───────────────────────────────────────────────╯  ╽    ╽
                                                                                        ◯   ┌╂┐▁▁┌╂┐
     {B}01110011{Z}  {B}110110{Z}   {B}111110{Z}  {B}1001110{Z}   {G}00{Z}       {G}10{Z}                      {G}00{Z}{P}             ₒ │ ■  ■ │
     {B}11{Z}       {B}11{Z}    {B}00{Z}    {B}01{Z}    {B}11{Z}    {B}10{Z}  {G}10{Z}   {G}1{Z}   {G}11{Z}                      {G}11{Z}{P}                ╲ ╰╯ ╱
     {B}10{Z}       {B}01{Z}    {B}01{Z}    {B}11{Z}    {B}00{Z}    {B}10{Z}  {G}00{Z}  {G}001{Z}  {G}00{Z}   {G}000000{Z}    {G}100000{Z}   {G}00{Z}    {G}10{Z}{P}          ▂▂┃┃▂▂    \)
     {B}10001{Z}    {B}00000100{Z}    {B}11{Z}    {B}0101011{Z}   {G}00{Z} {G}11{Z} {G}11{Z} {G}00{Z}  {G}{G}00{Z}    {G}00{Z}  {G}00{Z}    {G}10{Z}  {G}10{Z}   {G}00{Z}{P}        ░░▟██████▙░░ ▞
     {B}11{Z}       {B}11{Z}    {B}01{Z}    {B}00{Z}    {B}10{Z}    {B}00{Z}  {G}0110{Z}   {G}1337{Z}  {G}01{Z}    {G}00{Z}  {G}00{Z}        {G}011111{Z}{P}         ▞ ▜██████▛ ▚▞
     {B}11{Z}       {B}01{Z}    {B}10{Z}    {B}10{Z}    {B}00{Z}    {B}10{Z}  {G}110{Z}     {G}010{Z}  {G}00{Z}    {G}11{Z}  {G}00{Z}        {G}00{Z}   {G}10{Z}{P}       ▞    ▟▛▜▙
     {B}10{Z}       {B}00{Z}    {B}11{Z}  {B}010011{Z}  {B}01{Z}    {B}10{Z}  {G}10{Z}       {G}00{Z}   {G}010110{Z}   {G}00{Z}        {G}00{Z}    {G}42{Z}{P}     (\   ▟▛  ▜▙     
     """

if __name__ == '__main__':
    print(banner_sw)
    print(banner_color)
