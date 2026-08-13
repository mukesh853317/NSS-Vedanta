from database import init_db, get_connection
init_db()
conn = get_connection()

conn.execute("UPDATE settings SET college_name=?, nss_unit=?, programme_officer=?, academic_year=? WHERE id=1",
             ("Vedanta College", "NSS Unit", "NSS Programme Officer", "2026-27"))

volunteers = [
    ("NSS/2026/001","Aarav Patil","TYBCom","A","9000000001",""),
    ("NSS/2026/002","Ananya Sharma","SYBCom","B","9000000002",""),
    ("NSS/2026/003","Rohan More","TYBAF","A","9000000003",""),
]
for v in volunteers:
    try:
        conn.execute("""INSERT INTO volunteers(enrollment_no,name,class_name,division,mobile,email,joining_date,active)
                        VALUES(?,?,?,?,?,?,date('now'),1)""", v)
    except Exception:
        pass

try:
    conn.execute("""INSERT INTO activities
        (activity_code,title,activity_type,activity_date,venue,objectives,description,coordinator,beneficiaries,status,academic_year)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
        ("NSS-2026-001","Health Check-up Camp","Health Check-up","2026-09-24",
         "College Campus","Promote health awareness and preventive screening.",
         "Health check-up and awareness programme organised by the NSS Unit.",
         "NSS Programme Officer",185,"Planned","2026-27"))
except Exception:
    pass

conn.commit()
conn.close()
print("Demo data inserted.")
