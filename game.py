#!/usr/bin/env python3
import pygame
import ldap3

# Initialize Pygame
pygame.init()

# Set the size of the window
size = (700, 500)

# Create the window
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("Help Desk Interface")

# Create a list of options
options = ["LDAP", "Scripts"]

# Create a variable to store the current option
current_option = 0

# Create a list to store the rectangles of the options
option_rects = []

def home_button():
  # Create a new button surface and rect. You can use the pygame.Surface() method to create a new surface, and the pygame.Rect() method to create a new rect.
  home_button_surface = pygame.Surface((100, 50))
  home_button_rect = home_button_surface.get_rect(topleft=(20, 20))
  
  # Fill the surface with a color, and add text to it using the pygame.font module.
  home_button_surface.fill((255, 255, 255))
  home_button_text = font.render("Home", True, (0, 0, 0))
  home_button_surface.blit(home_button_text, (25, 15))

  # In the main loop, check if the mouse button is pressed and if the cursor is over the button rect.

  if event.type == pygame.MOUSEBUTTONDOWN and home_button_rect.collidepoint(event.pos):
      # Go back to the first page
      current_page = 'home'

  # Finally, in the render function, you can blit the button surface to the screen.
  screen.blit(home_button_surface, home_button_rect)



def page_ldap():
  # Create a variable to store the user input
  user_input = ""

  # Create a font object
  font = pygame.font.Font('./Arial Unicode.ttf', 30)
  # Draw the text box for user input
  text_box = pygame.Rect(10, 10, 300, 50)
  pygame.draw.rect(screen, (0, 0, 0), text_box)
  user_input_text = font.render(user_input, True, (0,0,0),(255, 255, 255))
  screen.blit(user_input_text, (text_box.x + 10, text_box.y + 10))

  # Draw the fetch button
  fetch_button = pygame.Rect(250, 200, 200, 50)
  pygame.draw.rect(screen, (0, 0, 0), fetch_button)
  fetch_button_text = font.render("Fetch from LDAP", True, (0,0,0),(255, 255, 255))
  screen.blit(fetch_button_text, (fetch_button.x + 10, fetch_button.y + 10))

  # Handle button events
  # Fetch from LDAP 
  # BIND="cn=ldap admin hinxton,cn=Admins,dc=embl,dc=org"
  # source ~/bin/.emblldap
  # exec ldapsearch -x -LLL -H ldaps://ldap.embl.de:636 -b dc=embl,dc=org -D "$BIND" -w "$PASS" "$@"
  if event.type == pygame.MOUSEBUTTONDOWN:
      if fetch_button.collidepoint(event.pos):
          # Connect to the LDAP server
          server = ldap3.Server('ldap.example.com')
          connection = ldap3.Connection(server)
          connection.bind()

          # Search for the user
          search_base = "ou=people,dc=example,dc=com"
          search_filter = "(uid=" + user_input + ")"
          attributes = ["jpegPhoto"]
          connection.search(search_base=search_base, search_filter=search_filter, attributes=attributes)

          # Get the jpegPhoto
          jpeg_photo = None
          if connection.entries:
              jpeg_photo = connection.entries[0].jpegPhoto.value

          if jpeg_photo:
              # Create a surface from the jpegPhoto
              image = pygame.image.fromstring(jpeg_photo, (150,200), "RGB")
              image = pygame.transform.scale(image, (150,200))
              screen.blit(image, (400,200))

          # Close the connection
          connection.unbind()


# Create a variable to store the current page
current_page = "main"

# Run the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_option = (current_option - 1) % len(options)
            elif event.key == pygame.K_DOWN:
                current_option = (current_option + 1) % len(options)
            elif event.key == pygame.K_RETURN:
                if current_page == "main":
                    if options[current_option] == "LDAP":
                        current_page = "ldap"
                    elif options[current_option] == "Scripts":
                        current_page = "scripts"
                else:
                    current_page = "main"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, option_rect in enumerate(option_rects):
                  if option_rect.collidepoint(event.pos):
                        if current_page == "main":
                            if options[i] == "LDAP":
                                current_page = "ldap"
                            elif options[i] == "Scripts":
                                current_page = "scripts"
                        else:
                            current_page = "main"
                            current_option = i
                            break
    # Clear the screen
    screen.fill((255, 255, 255))
    option_rects.clear()
    if current_page == "main":
        # Draw the options
        font = pygame.font.Font(None, 30)
        for i, option in enumerate(options):
            text = font.render(option, True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.y = screen.get_rect().height/3 + i*50

            if i == current_option:
                pygame.draw.rect(screen, (0,0,0), (text_rect.x-20, text_rect.y-20, text_rect.width+40, text_rect.height+40), 2)

            screen.blit(text, text_rect)
            option_rects.append(text_rect)
    elif current_page == "ldap":
        # Draw the LDAP page
        page_ldap()
        pass
    elif current_page == "scripts":
        # Draw the Scripts page
        pass

    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()