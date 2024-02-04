---
title: Workload Generation
author: Philipp Theyssen
---

Currently we are trying to create a configuration language
for expressing transaction workloads for a simulation framework.

This closely gets to language design, which is honestly really hard.

Also apart from that it suddenly feels that witph this freedom of
the design space I have to come up with a solution, make decisions
while coding, it is not immediately apparent which solution to chose.


Lets imagine you have a small expression like this:

```json
{
 "id": "operation-1",
 "http-method": "post",
 "returnValues": [
   {
     "key": "val-1",
     "value": "response.payload.table["first"]"
     "type": "object"

   }
 ]

}

```

Why am I writing this to clear my thoughts, and therefore
achieve clearer thinking about the problems having
myself express all the difficulties, forces me
to acknowledge the problems and list them.
This is not meant as guide or solution or even informed
opinion on the topic, but I invite you to do the same.


## Survey of different approaches

Tools like K6 also use very simplistic scheduler / execution of
workloads.

https://github.com/grafana/k6/blob/master/execution/scheduler.go


Open vs. closed model in K6 https://k6.io/docs/using-k6/scenarios/concepts/open-vs-closed/
- duration vs. goal rate
- starting rate / arrival rate


- Adjust workload execution based on application result (% of succesfull requests)
  -> actual throughput achieved
  - have threshold that monitors


## Submitting workload to orlean grains

want to stay below max concurrent threshold use
queue / pipeline?
