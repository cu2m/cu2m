********************************************************************************
**{title}**
********************************************************************************


================================================================================
Statistics
================================================================================

.. needpie:: Test Distribution
   :labels: Passed, Failed, Skipped
   :legend:
   :colors: green, red, grey

   '{id}' in tags and 'passed' == result and type=='{case_need}'
   '{id}' in tags and 'failure' == result and type=='{case_need}'
   '{id}' in tags and 'skipped' == result and type=='{case_need}'

.. list-table:: Tests Summary
   :widths: 60 40
   :header-rows: 1

   * - Name
     - Count

   * - Test suites
     - :need_count:`'{id}' in tags and type=='{suite_need}'`
   * - Test cases
     - :need_count:`'{id}' in tags and type=='{case_need}'`
   * - Failed test cases
     - :need_count:`'{id}' in tags and 'failure' == result and type=='{case_need}'`
   * - Skipped test cases
     - :need_count:`'{id}' in tags and 'skipped' == result and type=='{case_need}'`
   * - Passed test cases
     - :need_count:`'{id}' in tags and 'passed' == result and type=='{case_need}'`


================================================================================
Passed test cases
================================================================================

.. needtable::
   :filter: '{id}' in tags and 'passed' == result
   :columns: id, title, result
   :style_row: tr_[[copy('result')]]
   :filter_warning: No passed test cases


================================================================================
Failed test cases
================================================================================

.. needtable::
   :filter: '{id}' in tags and 'failure' == result
   :columns: id, title, result
   :style_row: tr_[[copy('result')]]
   :filter_warning: No failed test cases

================================================================================
Skipped test cases
================================================================================

.. needtable::
   :filter: '{id}' in tags and 'skipped' == result
   :columns: id, title, result
   :style_row: tr_[[copy('result')]]
   :filter_warning: No skipped test cases

.. .. test-results:: {file}


================================================================================
Detailed test results
================================================================================

.. {file_type}:: {title}
   :id: {id}{links_string}
   :tags: {tags}
   :file: {file}
   :auto_suites:
   :auto_cases:
   :collapse: FALSE