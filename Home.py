#importing modules
import streamlit as st 
from datetime import date

current_date = date.today()

st.title("Kağan Erkan")

st.write(f"Hi! My name is Kağan Erkan, I'm {current_date.year - 2009} years old currently. I make content on YouTube for fun, develop software, set up servers, and do more as a hobby in my free time from school.")

tab1,tab2 = st.tabs(["Bilfen Middle School","Bilfen Anatiolian High School"])
with tab1:
    st.write("I was at Bilfen Middle School. Here I learned about the world of programming via a school club. It wasn't anything more than basic algorithms at the club but a path was opened and I learned Lua, Python, and some algorithms these years. It's good to mention a scratch application that was a color-based test I developed at these times granted me a scholarship for the Tobb Etu Maker Program. ")
with tab2:
    st.write("Im currently at high school and still learning different things about life here. I'm actively searching for new information and thinking then combining what I learn at school with my computer and life experiences to get new project ideas for the near future.")

tab1,tab2 = st.tabs(["Code.org","Oyunumu Kodluyorum"])
with tab1:
    st.write("Participating in a coding club meant we needed to do something during these club hours so as a fast learner and a computer nerd I just got all the certificates that were available when I was at Middle School for the Code.org website. If I had told you it was hard or something worth a lot academically it would be a lie but since I was only at middle school up to this day it feels good knowing I got them.")
with tab2:
    st.write("Some time in middle school I decided to join this Game Jam that was made between Bilfen schools but we were eliminated because we lacked teamwork as we didn't think we would've needed it. This showed I would need good team and teamwork skills next time. So I started working on Git and how it worked and Git Hub alongside my team skills.")
 
tab1,tab2 = st.tabs(["Bilkent","Tob Ettu"])
with tab1:
    st.write("I got to Bilkent Summer Camp In 2024 and it was awesome. Education wasn't the best since it was for bigger level courses but it was a very good simulation of university life and preparation for the future.")
with tab2:
    st.write("I was in Tobb Ettu Maker's Program at middle school. It was as if a summer camp but we learned basic levels of programs that are used in real work spaces giving us a head start at the learning by giving us a boost on the hardest learning curve.")

tab1,tab2 = st.tabs(["Youtube","Instagram"])
with tab1:
    col1,col2 = st.columns(2)
    col1.link_button(label="Youtube Channel",url="https://www.youtube.com/channel/UCd7HC1eU_jV3EkAnlBkSXUQ",use_container_width=True)
    col2.link_button(label="Turkish Youtube Channel",url="https://www.youtube.com/@Kaganerkan",use_container_width=True)

with tab2:
    st.link_button("Instagram",url="https://www.instagram.com/kaganerkan_/",use_container_width=True)

