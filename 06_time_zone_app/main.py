import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Africa/Cairo",
    "Africa/Nairobi",
    "America/Chicago",
    "America/Toronto",
    "America/Vancouver",
    "Asia/Shanghai",
    "Asia/Singapore",
    "Asia/Seoul",
    "Asia/Ho_Chi_Minh",
    "Asia/Jakarta",
    "Asia/Bangkok",
    "Asia/Manila",
    "Europe/Paris",
    "Europe/Madrid",
    "Europe/Rome",
    "Europe/Amsterdam",
    "Europe/Brussels",
    "Europe/Moscow",
    "Europe/Istanbul",
    "Europe/Oslo",
    "Europe/Stockholm",
    "Europe/Helsinki",
    "Europe/Vienna",
    "Europe/Warsaw",
    "Europe/Zurich",
    "Europe/Athens",
    "Europe/Lisbon",
    "Europe/Dublin",
    "Europe/Copenhagen",
    "Europe/Prague",
    "Europe/Belgrade",
    "Europe/Budapest",
    "Europe/Bucharest",
    "Europe/Sofia",
    "Australia/Melbourne",
    "Australia/Perth",
    "Australia/Brisbane",
    "Australia/Adelaide",
    "Pacific/Auckland",
    "Pacific/Honolulu",
    "Pacific/Fiji",
    "Pacific/Guam",
    "Pacific/Tahiti",
    "Pacific/Pago_Pago",
    "America/Mexico_City",
    "America/Sao_Paulo",
    "America/Buenos_Aires",
    "America/Bogota",
    "America/Lima",
    "America/Caracas",
    "America/La_Paz",
    "America/Santiago",
    "America/Montevideo",
    "America/Asuncion",
    "America/Havana",
    "America/Denver",
    "America/Phoenix",
    "America/Anchorage",
    "America/Winnipeg",
    "America/Edmonton",
    "America/Guatemala",
    "America/Tegucigalpa",
    "America/Managua",
    "America/San_Juan",
    "Africa/Johannesburg",
    "Africa/Lagos",
    "Africa/Accra",
    "Africa/Nairobi",
    "Africa/Dakar",
    "Africa/Algiers",
    "Africa/Khartoum",
    "Africa/Kampala",
    "Africa/Dar_es_Salaam",
    "Africa/Maputo",
    "Africa/Harare",
    "Africa/Luanda",
    "Africa/Abidjan",
    "Asia/Riyadh",
    "Asia/Tehran",
    "Asia/Yangon",
    "Asia/Kathmandu",
    "Asia/Colombo",
    "Asia/Tashkent",
    "Asia/Ashgabat",
    "Asia/Almaty",
    "Asia/Dhaka",
    "Asia/Ulaanbaatar",
    "Asia/Novosibirsk",
    "Asia/Vladivostok",
    "Asia/Tbilisi",
    "Asia/Yerevan",
    "Asia/Kuwait",
    "Asia/Baku",
    "Asia/Muscat",
    "Asia/Qatar",
    "Asia/Beirut",
    "Asia/Damascus",
    "Asia/Baghdad",
    "Antarctica/McMurdo",
    "Antarctica/Palmer",
    "Antarctica/Rothera",
    "Antarctica/Troll",
]

st.set_page_config(page_title="Time zone", page_icon="⏲")
st.title("Time Zone App")

selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

st.subheader("Selected Timezones")
for tz in selected_timezone:

    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Converted Time"):

    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.success(f"Converted Time in {to_tz}: {converted_time}")

st.markdown("---")
st.write("Build by [Muhammad Kamran](https://github.com/KamranYT)")