import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import requests

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(page_title="I2IT College Chatbot", page_icon="🎓", layout="centered")

# =========================================================
# ENV SETUP
# =========================================================
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = "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"

# =========================================================
# SAMPLE LOCAL DATA
# =========================================================
qa_data = pd.DataFrame([
    {"query": "Where is the admission office?", "intent": "ask_location", "response": "The admission office is located in the Academic Block, Room A05."},
    {"query": "What is the admission process?", "intent": "ask_process", "response": "Online application, document verification, seat allotment via CAP and institute-level rounds."},
    {"query": "What are the eligibility criteria for B.Tech admission?", "intent": "ask_eligibility", "response": "12th with PCM and minimum 75% marks; JEE Mains or MHT-CET for selection."},
    {"query": "How many seats are available?", "intent": "ask_seats", "response": "Intake capacity is 140 students per department."},
    {"query": "Which courses are offered?", "intent": "ask_courses", "response": "Computer Engineering, Information Technology, Electronics & Telecommunication."},
    {"query": "What are the library timings?", "intent": "ask_time", "response": "8:30 AM to 9:00 PM (semester); 8:30 AM to 10:00 PM (exams)."},
    {"query": "Who is the HOD of Computer Science?", "intent": "ask_contact", "response": "Shitole Sir."},
    {"query": "Who is the HOD of IT?", "intent": "ask_contact", "response": "Jyoti Surve Mam."},
    {"query": "Who is the HOD of Electronics & Telecommunication?", "intent": "ask_contact", "response": "Mohan Naidu Sir ."},
    {"query": "Where is the boys' hostel?", "intent": "ask_location", "response": " Mithila Hostel Block, floors 3-7."},
    {"query": "Where is the girls' hostel?", "intent": "ask_location", "response": "Girls Hostel Block with 300 beds capacity."},
    {"query": "What are the hostel timings?", "intent": "ask_time", "response": "6:00 AM to 9:00 PM."},
    {"query": "What is the monthly canteen charge?", "intent": "ask_fee", "response": "₹3,600 per month."},
    {"query": "What scholarships are available?", "intent": "ask_scholarship", "response": "Post-Matric SC/ST/OBC/PWD, Karmaveer Bhaurao Patil Earn & Learn, and others."},
    {"query": "Who is the placement officer?", "intent": "ask_contact", "response": "Madhav Raul Sir."},
    {"query": "What is the tuition fee for B.Tech?", "intent": "ask_fee", "response": "Approx ₹1,20,000 per year."},
    {"query": "What are the office hours of the admission office?", "intent": "ask_time", "response": "8:30 AM to 4:00 PM, Monday to Friday."},
    {"query": "Where is the library located?", "intent": "ask_location", "response": "Library Block near the central of college."},
    {"query": "What is the exam timetable release date?", "intent": "ask_academic", "response": "Released 2 weeks before exams on college portal."},
    {"query": "What is the passing criteria for B.Tech?", "intent": "ask_academic", "response": "Minimum 40% marks in each subject."},
    {"query": "Where is the examination department?", "intent": "ask_location", "response": "PPCRC Block, Room P201."},
    {"query": "Is the exam section open on Saturdays?", "intent": "ask_time", "response": "No, it is closed on Saturdays."},
    {"query": "Where do I collect my hall ticket?", "intent": "ask_academic", "response": "Online student portal."},
    {"query": "Who is the librarian?", "intent": "ask_contact", "response": " Prabodhan Sir ."},
    {"query": "What are the mess timings?", "intent": "ask_time", "response": "Breakfast 8-10 AM, Lunch 1-2 PM, Dinner 8-9 PM."},
    {"query": "Are mobile phones allowed in the exam hall?", "intent": "ask_rules", "response": "Mobile phones are strictly prohibited."},
    {"query": "How do I apply for a scholarship?", "intent": "ask_process", "response": "Applications are submitted online via the college portal before deadlines."},
    {"query": "What are visitor rules for the hostel?", "intent": "ask_rules", "response": "Visitors must sign in; visiting hours 9 AM to 6 PM."},
    {"query": "Can parents visit the hostel?", "intent": "ask_rules", "response": "Yes, with prior permission during visiting hours."},
    {"query": "What is the emergency contact number?", "intent": "ask_rules", "response": "+91-9876543211."},
    {"query": "What transport options are available to campus?", "intent": "ask_transport", "response": "Public buses, cab services, and direct PMPL buses from Pune Station."},
    {"query": "Where is the placement cell?", "intent": "ask_contact", "response": "Placement Office near Administrative Block."},
    {"query": "What is the faculty strength?", "intent": "ask_info", "response": "Well qualified and experienced technical staff."},
    {"query": "Are there any student clubs?", "intent": "ask_activity", "response": "Yes, ACM Student Chapter, IEEE Student Branch, and more."},
    {"query": "What are library borrowing limits?", "intent": "ask_rules", "response": "2 books per borrower for 7 days; renewal once for 7 days."},
    {"query": "What resources are available in the library?", "intent": "ask_info", "response": "10,000+ books, journals, CDs/DVDs, databases including IEEE and J-Gate."},
    {"query": "What are the cultural activities?", "intent": "ask_events", "response": "Annual fest in January, student-organized events like Dhruva & Askara and multiple tech events are conducted."},
    {"query": "Where can I find seminar details?", "intent": "ask_events", "response": "Notice board or online portal with locations like Seminar Hall 1 in PPCRC."},
    {"query": "What is the code of conduct?", "intent": "ask_rules", "response": "Strict rules on discipline, privacy, and security enforced campus-wide."},
    {"query": "Where is the medical facility?", "intent": "ask_location", "response": "Health & Wellness Block near the main entrance."},
    {"query": "How do I get a bonafide certificate?", "intent": "ask_process", "response": "Applied at student services desk with student ID."},
    {"query": "Where is the canteen located?", "intent": "ask_location", "response": "Cafeteria Block is adjacent to the Academic Block , below the library."},
    {"query": "Who is the hostel warden?", "intent": "ask_contact", "response": "Ramesh Joshi."},
    {"query": "How can I register for hostel accommodation?", "intent": "ask_process", "response": "Online via student portal or hostel office."},
    {"query": "What are the facility timings for computer labs?", "intent": "ask_time", "response": "Academic Block, 2nd floor, Room A105; timings as per schedule."},
    {"query": "Is Wi-Fi available on campus?", "intent": "ask_info", "response": "Yes, campus-wide Wi-Fi for students and staff."},
    {"query": "How can I contact the administrative office?", "intent": "ask_contact", "response": "+91-9876543210 or visit Admin Office."},
    {"query": "What is the culture of the campus?", "intent": "ask_info", "response": "Emphasis on innovation, leadership, and life skills beyond academics."},
    {"query": "What are the sports facilities?", "intent": "ask_info", "response": "Gym, basketball and badminton courts in the Sports Complex."},
    {"query": "How do I escalate grievances?", "intent": "ask_process", "response": "Contact student grievance cell via official email or portal."},
])

data_dict = {"Students": qa_data}
successful_sheets = ["Students"]

# =========================================================
# STYLES
# =========================================================
st.markdown(
    """
<style>
body {
    background-color: #f5f8ff;
}
.chat-container {
    background-color: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
}
.user-msg {
    text-align: right;
    color: white;
    background-color: #004aad;
    padding: 0.7rem;
    border-radius: 10px;
    margin-bottom: 0.5rem;
}
.bot-msg {
    text-align: left;
    background-color: #111112;
    padding: 0.7rem;
    border-radius: 10px;
    margin-bottom: 0.5rem;
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# SIDEBAR
# =========================================================
# st.sidebar.image("logo.jpeg", width=120)
# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.image("logo.jpeg", width=120)
st.sidebar.markdown("""
### College Address
I²IT Campus, Hinjewadi Phase 1 , Pune ,  Maharashtra, India - 411057

### Contact Number
📞 +91-9876543210

### Accreditation
🏆 NAAC Accredited - Grade A
""")

# =========================================================
# PAGE HEADER
# =========================================================
st.title(" I²IT College")
#st.caption("Ask questions about students, faculty, or general college info.")
st.markdown("---")

# =========================================================
# SESSION STATE
# =========================================================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "history_limit" not in st.session_state:
    st.session_state.history_limit = 8

# =========================================================
# LOCAL SEARCH
# =========================================================
def search_local_data(query):
    data = data_dict.get("Students")
    if data is not None:
        lowered = query.lower()
        matches = data[data["query"].str.lower().str.contains(lowered)]
        if not matches.empty:
            return matches.iloc[0]["response"]
    return None

# =========================================================
# GROQ API CALL
# =========================================================
def get_groq_response(history):
    if not GROQ_API_KEY:
        return "⚠️ Missing GROQ API key."

    df_students = data_dict.get("Students")
    if df_students is not None:
        try:
            student_data_str = df_students.head(50).to_csv(index=False)
        except Exception:
            student_data_str = "<student table unavailable>"
    else:
        student_data_str = "No student data available."

    system_prompt = (
    "You are the official I²IT College chatbot assistant. "
    "Your task is to provide clear, accurate, and polite responses to user queries related to I²IT College. "
    "Use the provided student data to inform your answers whenever relevant and available. "
    "If information is not found in the data, respond politely saying ask the security for more info."
    "\n\n"
    f"{student_data_str}\n"
)


    messages = [{"role": "system", "content": system_prompt}]
    for msg in history[-st.session_state.history_limit:]:
        messages.append({"role": "user", "content": msg})

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": "llama-3.1-8b-instant", "messages": messages}

    try:
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=15,
        )
        if res.status_code == 200:
            return res.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        else:
            return f"⚠️ Error: {res.status_code} - {res.text}"
    except Exception as e:
        return f"⚠️ API request failed: {e}"

# =========================================================
# INPUT AND RESPONSE HANDLING
# =========================================================
user_input = st.text_input("Want to know Info ? Ask here:")

if user_input:
    st.session_state.chat_history.append(user_input)
    local_answer = search_local_data(user_input)
    if local_answer:
        response = local_answer
    else:
        response = get_groq_response(st.session_state.chat_history)
    st.session_state.chat_history.append(response)

# =========================================================
# DISPLAY CHAT
# =========================================================
for i, msg in enumerate(st.session_state.chat_history):
    if i % 2 == 0:
        st.markdown(f"<div class='user-msg'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg}</div>", unsafe_allow_html=True)

st.markdown("---")
#st.markdown("<center>Developed with ❤️ by I2IT Pune</center>", unsafe_allow_html=True)



