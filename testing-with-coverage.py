import coverage

cov = coverage.Coverage()
cov.start()

# do the code here

cov.stop()
cov.save()

cov.html_report()