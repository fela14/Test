def pytest_addoption(parser):
    """Add a '--nice' option to turn failures into opportunities."""
    group = parser.getgroup('nice')
    group.addoption(
        "--nice",
        action="store_true",
        help="Turn failures into opportunities"
    )

def pytest_report_header(config):
    """Add a header message if --nice is enabled."""
    if config.getoption('nice'):
        return "Thanks for running the tests."

def pytest_report_teststatus(report, config):
    """Turn failures into 'opportunities' if --nice is enabled."""
    if report.when == "call" and report.failed and config.getoption('nice'):
        return (report.outcome, "O", "OPPORTUNITY for improvement")
