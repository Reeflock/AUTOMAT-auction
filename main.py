import pixelReadS as pr
import macro
import windowget as wg

from time import sleep

def main(number_of_tries = 1):

    if number_of_tries == 0:
        number_of_tries = 1
        reduction = 0
    else:
        reduction = 1

    wg.activateWindow("Forza Horizon 6")
    sleep(1)
    auction_pixel = pr.PixelRead(1562,177,0xCAFF02)
    ac_menu_pixel = pr.PixelRead(1261,649,0XFFFFFF)
    original_tries = number_of_tries

    while number_of_tries >= 1:

        macro.menu_to_auction()
        for i in range(90):
            if auction_pixel.read_pixel():
                
                for n in range(80):
                    macro.y_spam()
                    if ac_menu_pixel.read_pixel():
                        macro.buyout()
                        print(f"Finished Succesfully within {(original_tries-number_of_tries)+1} tries")
                        number_of_tries = -1
                        
                        break
                    else:
                        continue
                break   
            else:
                
                continue
            
        macro.esc()
        number_of_tries = number_of_tries - reduction
    if number_of_tries == -1:
        print(f" Total Runs {(original_tries-number_of_tries)+1}")
    else:
        print(f" Total Runs {(original_tries-number_of_tries)}")
    print("Completed")

if __name__ == '__main__':
    cycles = int(input("Enter the number of tries (enter 0 for infinity): "))
    main(cycles)
                