from __future__ import print_function
import datetime
import sys
import time
from wpc.audit import Audit, Dump, DumpTab
from wpc.report import Report
from wpc.parseOptions import parse_options
import wpc.utils


def main():
    # Parse command line arguments
    options = parse_options()

    # Initialise WPC
    # TODO be able to enable/disable caching
    wpc.utils.init(options)

    # Object to hold all the issues we find
    report = Report()
    wpc.utils.populate_scaninfo(report)
    issues = report.get_issues()

    if options.pyshell_mode:
        wpc.utils.printline("Python Shell - to exit do CTRL-z or type exit()")
        print()
        import code
        code.interact(local=dict(globals(), **locals()))
        sys.exit()

    wpc.utils.dump_options(options)

    wpc.utils.printline("Starting Audit at %s" %
                        datetime.datetime.strftime(datetime.datetime.now(),
                                                   '%Y-%m-%d %H:%M:%S'))
    start_time = time.time()

    # Dump raw data if required
    if options.dump_mode:
        d = Dump(options)
        d.run()

    # Dump raw data if required
    if options.dumptab_mode:
        d = DumpTab(options, report)
        d.run()

    # Identify security issues
    if options.audit_mode:
        a = Audit(options, report)
        a.run()

        if options.report_file_stem:
            wpc.utils.printline("Audit Complete at %s" % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
            print()
            print("[+] Runtime: %.1f seconds" % int(time.time() - start_time))
            print()

            filename = "%s.xml" % options.report_file_stem
            print("[+] Saving report file %s" % filename)
            f = open(filename, 'w')
            f.write(report.as_xml_string())
            f.close()

            filename = "%s.txt" % options.report_file_stem
            print("[+] Saving report file %s" % filename)
            f = open(filename, 'w')
            f.write(report.as_text())
            f.close()

            filename = "%s.html" % options.report_file_stem
            print("[+] Saving report file %s" % filename)
            f = open(filename, 'w')
            f.write(report.as_html())
            f.close()

    #wpc.conf.cache.print_stats()


if __name__ == '__main__':
    main()
