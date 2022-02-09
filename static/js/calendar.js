function yearleepy(year) {
  return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
}
function printCalendar() {
  data = new Date();

  let year = data.getYear();
  if (year < 1000) year = 2000 + year - 100;

  const month = data.getMonth() + 1;
  const weekDay = data.getDay();
  const monthDay = data.getDate();

  const tempDate = new Date(year, month - 1, 1);
  const firstDayMonth = tempDate.getDay();

  if (weekDay == 0) weekDay = 7;
  if (firstDayMonth == 0) firstDayMonth = 7;

  switch (month) {
    case 1:
      monthName = "January";
      daysInMonth = 31;
      break;
    case 2:
      monthName = "February";
      daysInMonth = yearleepy(year) ? 29 : 28;
      break;
    case 3:
      monthName = "March";
      daysInMonth = 31;
      break;
    case 4:
      monthName = "April";
      daysInMonth = 30;
      break;
    case 5:
      monthName = "May";
      daysInMonth = 31;
      break;
    case 6:
      monthName = "June";
      daysInMonth = 30;
      break;
    case 7:
      monthName = "July";
      daysInMonth = 31;
      break;
    case 8:
      monthName = "August";
      daysInMonth = 31;
      break;
    case 9:
      monthName = "September";
      daysInMonth = 30;
      break;
    case 10:
      monthName = "October";
      daysInMonth = 31;
      break;
    case 11:
      monthName = "November";
      daysInMonth = 30;
      break;
    case 12:
      monthName = "December";
      daysInMonth = 31;
      break;
  }

  document.write("<TABLE border = 1><TR>");
  document.write("<TD bgcolor='#a5c422' align='center' colspan='7'>");
  document.write(monthName + " " + year);
  document.write("</TD></TR><TR>");

  document.write("<TR>");
  document.write("<TD align='center' bgcolor='pink'>M</TD>");
  document.write("<TD align='center' bgcolor='pink'>T</TD>");
  document.write("<TD align='center' bgcolor='pink'>W</TD>");
  document.write("<TD align='center' bgcolor='pink'>T</TD>");
  document.write("<TD align='center' bgcolor='pink'>F</TD>");
  document.write("<TD align='center' bgcolor='pink'>S</TD>");
  document.write("<TD align='center' bgcolor='pink'>S</TD>");
  document.write("</TR>");

  var j = daysInMonth + firstDayMonth - 1;

  for (var i = 0; i < j; i++) {
    if (i < firstDayMonth - 1) {
      document.write("<TD bgcolor='white'></TD>");
      continue;
    }
    if (i % 7 == 0) {
      document.write("</TR><TR>");
    }
    if (i - firstDayMonth + 2 == monthDay) {
      color = "#a5c422";
    } else {
      color = "#f9f9f9";
    }
    document.write("<TD bgcolor='" + color + "' align='center'>");
    document.write(i - firstDayMonth + 2);
    document.write("</TD>");
  }
  document.write("</TR></TABLE>");
}
