from xml.dom import minidom

doc = minidom.parse("Challenge1/data/wsu.xml")

root = doc.documentElement

courses = root.getElementsByTagName("course")

for course in courses:
    sln = course.getElementsByTagName("sln")[0].firstChild.data if course.getElementsByTagName("sln")[0].firstChild else ""
    prefix = course.getElementsByTagName("prefix")[0].firstChild.data
    course_number = course.getElementsByTagName("crs")[0].firstChild.data
    section = course.getElementsByTagName("sect")[0].firstChild.data
    title = course.getElementsByTagName("title")[0].firstChild.data
    credits = course.getElementsByTagName("credit")[0].firstChild.data if course.getElementsByTagName("credit")[0].firstChild else ""
    days = course.getElementsByTagName("days")[0].firstChild.data if course.getElementsByTagName("days")[0].firstChild else ""
    start_time = course.getElementsByTagName("start")[0].firstChild.data if course.getElementsByTagName("start")[0].firstChild else ""
    building = course.getElementsByTagName("bldg")[0].firstChild.data
    room = course.getElementsByTagName("room")[0].firstChild.data if course.getElementsByTagName("room")[0].firstChild else ""
    instructor = course.getElementsByTagName("instructor")[0].firstChild.data if course.getElementsByTagName("instructor")[0].firstChild else ""
    limit = course.getElementsByTagName("limit")[0].firstChild.data
    enrolled = course.getElementsByTagName("enrolled")[0].firstChild.data

    print(f"Course SLN: {sln}")
    print(f"Prefix: {prefix}")
    print(f"Course Number: {course_number}")
    print(f"Section: {section}")
    print(f"Title: {title}")
    print(f"Credits: {credits}")
    print(f"Days: {days}")
    print(f"Start Time: {start_time}")
    print(f"Building: {building}")
    print(f"Room: {room}")
    print(f"Instructor: {instructor}")
    print(f"Limit: {limit}")
    print(f"Enrolled: {enrolled}")
    print("\n")
    print("-" * 30)
    print("\n")






    
    


