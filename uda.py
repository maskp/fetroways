# # #import following modules
# # import webbrowser
# # import time
# #
# # #use the for loop to repeat the action 3 times
# # for i in range(0,3):
# # #sleep method of time is used to open the videos
# #   time.sleep(10)
# #   webbrowser.open('https://www.youtube.com/watch?v=NLDGekeZh_8');
#
# import turtle
# def makeTurtle():
#     window= turtle.Screen();
#     window.bgcolor('brown')
#
#
#
# def draw_sq():
#     makeTurtle();
#     mac = turtle.Turtle();
#     mac.speed(1);
#     mac.shape('turtle')
#     i=0
#     while i<4:
#         mac.forward(100);
#         mac.right(90);
#         i+=1
#
# def draw_c():
#     makeTurtle();
#     mac = turtle.Turtle();
#     mac.speed(1);
#     mac.shape('turtle');
#     mac.circle(50)
#
# def draw_t():
#     makeTurtle()
#     jar = turtle.Turtle();
#     jar.speed(1)
#     jar.shape('turtle');
#     i=0
#     while i<3:
#         jar.left(80)
#         jar.forward(100);
#         jar.left(45)
#         i+=1
#
#
# draw_sq();
# draw_c();
# draw_t();
import media
print(media.bands.__name__);

# from twilio.rest import TwilioRestClient
#
# account_sid = "{{ account_sid }}" # Your Account SID from www.twilio.com/console
# auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console
#
# client = TwilioRestClient(account_sid, auth_token)
#
# message = client.messages.create(body="Hello from Python",
#     to="+12345678901",    # Replace with your phone number
#     from_="+12345678901") # Replace with your Twilio number
#
# print(message.sid)
