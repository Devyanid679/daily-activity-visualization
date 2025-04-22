import matplotlib.pyplot as plt
import seaborn as sns 

# Create a simple dataset 
activities = ['Sleep', 'Study', 'Gym', 'Screen Time', 'Eating', 'Free Time', 'Other']
hours = [7, 4, 1, 4, 2, 3, 3]

# Create a bar plot
plt.figure(figsize=(8, 5))  
sns.barplot(x=activities, y=hours, palette='viridis') 

# Add a title and labels to the bar chart
plt.title('Daily Time Spent on Activities')  # Title of the chart
plt.xlabel('Activities')  # Label for the x-axis
plt.ylabel('Hours')  # Label for the y-axis

# Rotate x-axis labels and adjust the layout
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.tight_layout()  # Adjusts the layout to make sure everything fits properly

# Create a pie chart
plt.figure(figsize=(6, 6))  # Set the figure size (optional)
plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))  # Create the pie chart
plt.title('Daily Activity Distribution')  # Title of the pie chart
plt.axis('equal')  # This ensures the pie chart is circular

# Display both charts
plt.show()  # Show both the bar chart and pie chart together
