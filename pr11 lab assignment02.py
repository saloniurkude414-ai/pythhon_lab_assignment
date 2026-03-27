import matplotlib.pyplot as plt

companies = ["Microsoft","Google","Amazon","IBM","Deloitte","Capgemini","ATOS","Amdocs"]
recruitments = [120,150,180,90,110,130,70,95]

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Recruitments in Companies")
plt.xticks(rotation=30)
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Share")
plt.show()

# c) Customized Pie Chart
colors = ['red','blue','green','yellow','orange','purple','pink','cyan']
plt.pie(recruitments, labels=companies, colors=colors, autopct='%1.1f%%', shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.5,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# Comparison IBM vs Amdocs
labels = ["IBM","Amdocs"]
values = [90,95]

plt.bar(labels, values)
plt.title("IBM vs Amdocs Recruitment")
plt.show()