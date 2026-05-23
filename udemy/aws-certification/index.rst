AWS Professional Certifications
===============================

Solutions Architect Professional
--------------------------------

Exam
~~~~

* https://www.aws.training/Certification

Course Material
~~~~~~~~~~~~~~~

* `Slides v2.2.1 <https://media.datacumulus.com/aws-sap/AWS%20Certified%20Solutions%20Architect%20Professional%20Slides%20v2.2.1.pdf>`_

Practice Exams
~~~~~~~~~~~~~~

* https://www.udemy.com/course/practice-exam-aws-certified-solutions-architect-professional/
* https://www.udemy.com/course/aws-certified-solutions-architect-professional-aws-practice-exams/

Reference Notes
~~~~~~~~~~~~~~~

**CloudWatch Logs for Lambda**

- Lambda auto-reports metrics to CloudWatch.
- After permissions are set, Lambda logs all requests and stores code-generated logs in CloudWatch Logs.
- Log group: ``/aws/lambda/<function-name>``
- View via Lambda console, CloudWatch console, AWS CLI, or CloudWatch API.

**Lambda + X-Ray**

- X-Ray visualizes app components, bottlenecks, and error traces.
- Lambda sends trace data when X-Ray tracing is enabled upstream (API Gateway, EC2 with X-Ray SDK).
- Upstream service samples requests and passes a tracing header.

.. image:: /_static/aws-systems-manager.png


DevOps Professional
-------------------

Exam Link
~~~~~~~~~

* https://www.aws.training/Certification

Course Material
~~~~~~~~~~~~~~~

* `Link to Slides <https://courses.datacumulus.com/downloads/certified-devops-engineer-professional-h3e/>`_

Practice Exam
~~~~~~~~~~~~~

* `Practice Exam <https://www.udemy.com/course/aws-certified-devops-engineer-professional-practice-exam-dop/?couponCode=NOV_22_GET_STARTED>`_
