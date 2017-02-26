Title: HTTP benchmarking with Bombardier
Date: 2017-02-26 12:10
Category: Tools
Tags: http-benchmarking, github, load-testing

HTTP benchmarking is an important step in the life cycle of the development of a piece of software, especially with the ever growing popularity of REST apis over HTTP. To address this, I would like to share my discovery of the day.

## Http benchmarking with Bombardier

[Bombardier](https://github.com/codesenberg/bombardier) is a command-line HTTP(s) benchmarking tool written in GO and hosted on github, a nice alternative to Apache AB someone told me about earlier today. I think it's a great tool to have a quick overview of how an endpoint of your application server is responding to a high load. It is lightweight, fast and straight to the point.

## Installation

You will need to have go installed (obviously), version 1.6 or higher but having at least 1.7 is being preferred, have your GOPATH exported, and then run:

```
go get -u github.com/codesenberg/bombardier
```

The binary `bombardier` will be then available in your `$GOPATH/bin` path, make sure it is exported in your `$PATH`.

## Usage

The usage extremely simple, without any parameters it will use by default 125 concurrent connections for a duration of 10 seconds:

```
bombardier {{url}}
```

The output is short but complete, you will have statistics about the number of requests per seconds and latency, the throughput, and each requests will be grouped by HTTP codes so that you can actually see if amongst all those requests a couple of them failed miserably.

Example output:

```
➜  ~ bombardier http://localhost:5000/health
Bombarding http://localhost:5000/payment for 10s using 125 connections
[=============================================================================================] 10s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec       679.00      42.54        730
  Latency      182.45ms    16.27ms   252.95ms
  HTTP codes:
    1xx - 0, 2xx - 0, 3xx - 6918, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   352.04KB/s
```

Some of the most useful options are:

 * `-c {{number}}` to set the maximum number of concurrent connections
 * `-t {{number}}` to set the socket/request timeout
 * `-d {{number}}` to set the duration of the test

Example:

```
bombardier -c 500 -t 1 -d 30 http://localhost:5000/health
```

But there are much more and you can get the complete list of options by running:

```
bombardier --help
```
 
## My two cents

This tool is great to quickly run a load test on a specific endpoint and get useful information fast and in a non cryptic way (I am looking at you `ab`). But unfortunately, it is limited to a single URL and there are no reports that can be generated/exported (at the time I am writing those lines). I hope we will get this reporting feature pretty soon as the project seems healthy and development ongoing: commits are frequent and tickets are being closed quickly (with an actual solution); I would love to keep historical information about an endpoint and present the improvements over time to whoever has time for me.
