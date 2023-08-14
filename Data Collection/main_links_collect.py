from bs4 import BeautifulSoup
from openpyxl import Workbook

def extract_links_to_excel(html, filename):
    # Create a BeautifulSoup object from the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Create an empty list to store the links
    links = []

    # Find all the <a> tags in the HTML and extract the href attribute
    for a in soup.find_all('a'):
        href = a.get('href')
        if href is not None:
            links.append(href)

    # Create a new Excel workbook and worksheet
    wb = Workbook()
    sheet = wb.active

    # Write the links to the worksheet
    for i, link in enumerate(links):
        sheet.cell(row=i+1, column=1, value=link)

    # Save the workbook to disk
    wb.save(filename)

html_code = """
	<!DOCTYPE html>
	<html>
	<head>
		<title>Sample Page</title>
	</head>
	<body>
		<p><a href="http://www.millersmiles.co.uk/archives/300">14th April 2015 - 15th May 2015</a>
		<a href="http://www.millersmiles.co.uk/archives/299">4th March 2015 - 14th April 2015</a>
		<a href="http://www.millersmiles.co.uk/archives/298">28th January 2015 - 4th March 2015</a>
		<a href="http://www.millersmiles.co.uk/archives/297">27th January 2015 - 28th January 2015</a>
		<a href="http://www.millersmiles.co.uk/archives/296">23rd October 2014 - 27th January 2015</a>
		<a href="http://www.millersmiles.co.uk/archives/295">3rd September 2014 - 23rd October 2014</a>
		<a href="http://www.millersmiles.co.uk/archives/294">15th July 2014 - 2nd September 2014</a>
		<a href="http://www.millersmiles.co.uk/archives/293">24th May 2014 - 15th July 2014</a>
		<a href="http://www.millersmiles.co.uk/archives/292">8th April 2014 - 24th May 2014</a>
		<a href="http://www.millersmiles.co.uk/archives/291">26th February 2014 - 8th April 2014</a>
		<a href="http://www.millersmiles.co.uk/archives/290">20th January 2014 - 24th February 2014</a>
		<a href="http://www.millersmiles.co.uk/archives/289">2nd December 2013 - 19th January 2014</a>
		<a href="http://www.millersmiles.co.uk/archives/288">29th September 2013 - 2nd December 2013</a>
		<a href="http://www.millersmiles.co.uk/archives/287">11th August 2013 - 29th September 2013</a>
		<a href="http://www.millersmiles.co.uk/archives/286">17th June 2013 - 11th August 2013</a>
		<a href="http://www.millersmiles.co.uk/archives/285">20th April 2013 - 16th June 2013</a>
		<a href="http://www.millersmiles.co.uk/archives/284">20th February 2013 - 19th April 2013</a>
		<a href="http://www.millersmiles.co.uk/archives/283">20th December 2012 - 18th February 2013</a>
		<a href="http://www.millersmiles.co.uk/archives/282">14th November 2012 - 20th December 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/281">16th October 2012 - 13th November 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/280">18th September 2012 - 16th October 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/279">24th August 2012 - 18th September 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/278">28th July 2012 - 24th August 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/277">29th June 2012 - 28th July 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/276">31st May 2012 - 28th June 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/275">10th May 2012 - 31st May 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/274">18th April 2012 - 9th May 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/273">30th March 2012 - 18th April 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/272">6th March 2012 - 29th March 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/271">18th February 2012 - 6th March 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/270">1st February 2012 - 18th February 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/269">15th January 2012 - 1st February 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/268">30th December 2011 - 15th January 2012</a>
		<a href="http://www.millersmiles.co.uk/archives/267">8th December 2011 - 30th December 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/266">25th November 2011 - 8th December 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/265">14th November 2011 - 24th November 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/264">2nd November 2011 - 13th November 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/263">23rd October 2011 - 2nd November 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/262">12th October 2011 - 23rd October 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/261">2nd October 2011 - 12th October 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/260">20th September 2011 - 1st October 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/259">8th September 2011 - 20th September 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/258">29th August 2011 - 8th September 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/257">18th August 2011 - 29th August 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/256">9th August 2011 - 18th August 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/255">2nd August 2011 - 9th August 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/254">25th July 2011 - 2nd August 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/253">19th July 2011 - 25th July 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/252">11th July 2011 - 19th July 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/251">2nd July 2011 - 11th July 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/250">23rd June 2011 - 2nd July 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/249">9th June 2011 - 23rd June 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/248">27th May 2011 - 9th June 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/247">17th May 2011 - 27th May 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/246">1st May 2011 - 16th May 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/245">19th April 2011 - 1st May 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/244">10th April 2011 - 19th April 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/243">31st March 2011 - 10th April 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/242">21st March 2011 - 31st March 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/241">12th March 2011 - 21st March 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/240">2nd March 2011 - 11th March 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/239">20th February 2011 - 1st March 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/238">12th February 2011 - 19th February 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/237">7th February 2011 - 12th February 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/236">2nd February 2011 - 7th February 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/235">31st January 2011 - 2nd February 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/234">21st January 2011 - 31st January 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/233">14th January 2011 - 21st January 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/232">9th January 2011 - 14th January 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/231">28th December 2010 - 9th January 2011</a>
		<a href="http://www.millersmiles.co.uk/archives/230">20th December 2010 - 28th December 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/229">11th December 2010 - 20th December 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/228">5th December 2010 - 11th December 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/227">28th November 2010 - 5th December 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/226">22nd November 2010 - 28th November 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/225">16th November 2010 - 22nd November 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/224">10th November 2010 - 16th November 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/223">4th November 2010 - 10th November 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/222">29th October 2010 - 4th November 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/221">22nd October 2010 - 29th October 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/220">15th October 2010 - 22nd October 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/219">9th October 2010 - 15th October 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/218">3rd October 2010 - 9th October 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/217">29th September 2010 - 3rd October 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/216">26th September 2010 - 29th September 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/215">18th September 2010 - 26th September 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/214">12th September 2010 - 18th September 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/213">6th September 2010 - 12th September 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/212">30th August 2010 - 6th September 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/211">24th August 2010 - 30th August 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/210">19th August 2010 - 24th August 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/209">13th August 2010 - 19th August 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/208">8th August 2010 - 13th August 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/207">3rd August 2010 - 8th August 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/206">29th July 2010 - 3rd August 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/205">24th July 2010 - 29th July 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/204">18th July 2010 - 24th July 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/203">11th July 2010 - 18th July 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/202">4th July 2010 - 11th July 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/201">28th June 2010 - 4th July 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/200">21st June 2010 - 28th June 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/199">14th June 2010 - 21st June 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/198">8th June 2010 - 14th June 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/197">2nd June 2010 - 8th June 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/196">28th May 2010 - 2nd June 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/195">21st May 2010 - 28th May 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/194">17th May 2010 - 21st May 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/193">11th May 2010 - 16th May 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/192">6th May 2010 - 11th May 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/191">2nd May 2010 - 6th May 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/190">27th April 2010 - 2nd May 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/189">20th April 2010 - 27th April 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/188">15th April 2010 - 20th April 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/187">8th April 2010 - 15th April 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/186">1st April 2010 - 8th April 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/185">26th March 2010 - 1st April 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/184">21st March 2010 - 26th March 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/183">15th March 2010 - 21st March 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/182">9th March 2010 - 15th March 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/181">5th March 2010 - 9th March 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/180">28th February 2010 - 5th March 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/179">23rd February 2010 - 28th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/178">20th February 2010 - 22nd February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/177">20th February 2010 - 20th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/176">19th February 2010 - 20th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/175">19th February 2010 - 19th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/174">19th February 2010 - 19th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/173">18th February 2010 - 19th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/172">18th February 2010 - 18th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/171">17th February 2010 - 18th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/170">17th February 2010 - 17th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/169">16th February 2010 - 17th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/168">16th February 2010 - 16th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/167">15th February 2010 - 16th February 2010</a>
		6<a href="http://www.millersmiles.co.uk/archives/166">15th February 2010 - 15th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/165">14th February 2010 - 15th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/164">14th February 2010 - 14th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/163">13th February 2010 - 14th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/162">13th February 2010 - 13th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/161">12th February 2010 - 13th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/160">12th February 2010 - 12th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/159">11th February 2010 - 12th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/158">11th February 2010 - 11th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/157">11th February 2010 - 11th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/156">10th February 2010 - 11th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/155">10th February 2010 - 10th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/154">9th February 2010 - 10th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/153">9th February 2010 - 9th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/152">9th February 2010 - 9th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/151">8th February 2010 - 9th February 2010</a>
		<a href="http://www.millersmiles.co.uk/archives/150">8th February 2010 - 8th February 2010</a><a href="http://www.millersmiles.co.uk/archives/149">7th February 2010 - 8th February 2010</a><a href="http://www.millersmiles.co.uk/archives/148">7th February 2010 - 7th February 2010</a><a href="http://www.millersmiles.co.uk/archives/147">6th February 2010 - 7th February 2010</a>6<a href="http://www.millersmiles.co.uk/archives/146">6th February 2010 - 6th February 2010</a><a href="http://www.millersmiles.co.uk/archives/145">5th February 2010 - 6th February 2010</a><a href="http://www.millersmiles.co.uk/archives/144">5th February 2010 - 5th February 2010</a><a href="http://www.millersmiles.co.uk/archives/143">1st February 2010 - 5th February 2010</a><a href="http://www.millersmiles.co.uk/archives/142">28th January 2010 - 1st February 2010</a><a href="http://www.millersmiles.co.uk/archives/141">23rd January 2010 - 28th January 2010</a><a href="http://www.millersmiles.co.uk/archives/140">19th January 2010 - 23rd January 2010</a><a href="http://www.millersmiles.co.uk/archives/139">13th January 2010 - 19th January 2010</a><a href="http://www.millersmiles.co.uk/archives/138">8th January 2010 - 13th January 2010</a><a href="http://www.millersmiles.co.uk/archives/137">3rd January 2010 - 8th January 2010</a>6<a href="http://www.millersmiles.co.uk/archives/136">27th December 2009 - 3rd January 2010</a><a href="http://www.millersmiles.co.uk/archives/135">19th December 2009 - 27th December 2009</a><a href="http://www.millersmiles.co.uk/archives/134">15th December 2009 - 18th December 2009</a><a href="http://www.millersmiles.co.uk/archives/133">10th December 2009 - 15th December 2009</a><a href="http://www.millersmiles.co.uk/archives/132">6th December 2009 - 10th December 2009</a><a href="http://www.millersmiles.co.uk/archives/131">1st December 2009 - 5th December 2009</a><a href="http://www.millersmiles.co.uk/archives/130">26th November 2009 - 30th November 2009</a><a href="http://www.millersmiles.co.uk/archives/129">20th November 2009 - 26th November 2009</a><a href="http://www.millersmiles.co.uk/archives/128">16th November 2009 - 20th November 2009</a><a href="http://www.millersmiles.co.uk/archives/127">11th November 2009 - 16th November 2009</a><a href="http://www.millersmiles.co.uk/archives/126">8th November 2009 - 11th November 2009</a><a href="http://www.millersmiles.co.uk/archives/125">4th November 2009 - 8th November 2009</a><a href="http://www.millersmiles.co.uk/archives/124">31st October 2009 - 4th November 2009</a><a href="http://www.millersmiles.co.uk/archives/123">26th October 2009 - 31st October 2009</a><a href="http://www.millersmiles.co.uk/archives/122">21st October 2009 - 26th October 2009</a><a href="http://www.millersmiles.co.uk/archives/121">15th October 2009 - 21st October 2009</a><a href="http://www.millersmiles.co.uk/archives/120">11th October 2009 - 15th October 2009</a><a href="http://www.millersmiles.co.uk/archives/119">5th October 2009 - 11th October 2009</a><a href="http://www.millersmiles.co.uk/archives/118">30th September 2009 - 5th October 2009</a><a href="http://www.millersmiles.co.uk/archives/117">26th September 2009 - 30th September 2009</a><a href="http://www.millersmiles.co.uk/archives/116">21st September 2009 - 26th September 2009</a><a href="http://www.millersmiles.co.uk/archives/115">16th September 2009 - 20th September 2009</a><a href="http://www.millersmiles.co.uk/archives/114">12th September 2009 - 16th September 2009</a><a href="http://www.millersmiles.co.uk/archives/113">8th September 2009 - 11th September 2009</a><a href="http://www.millersmiles.co.uk/archives/112">7th September 2009 - 8th September 2009</a><a href="http://www.millersmiles.co.uk/archives/111">7th September 2009 - 7th September 2009</a><a href="http://www.millersmiles.co.uk/archives/110">27th August 2009 - 7th September 2009</a><a href="http://www.millersmiles.co.uk/archives/109">23rd August 2009 - 27th August 2009</a><a href="http://www.millersmiles.co.uk/archives/108">19th August 2009 - 23rd August 2009</a><a href="http://www.millersmiles.co.uk/archives/107">16th August 2009 - 19th August 2009</a><a href="http://www.millersmiles.co.uk/archives/106">11th August 2009 - 16th August 2009</a><a href="http://www.millersmiles.co.uk/archives/105">7th August 2009 - 11th August 2009</a><a href="http://www.millersmiles.co.uk/archives/104">3rd August 2009 - 7th August 2009</a><a href="http://www.millersmiles.co.uk/archives/103">27th July 2009 - 2nd August 2009</a><a href="http://www.millersmiles.co.uk/archives/102">21st July 2009 - 27th July 2009</a><a href="http://www.millersmiles.co.uk/archives/101">14th July 2009 - 21st July 2009</a><a href="http://www.millersmiles.co.uk/archives/100">9th July 2009 - 14th July 2009</a><a href="http://www.millersmiles.co.uk/archives/99">7th July 2009 - 9th July 2009</a><a href="http://www.millersmiles.co.uk/archives/98">3rd July 2009 - 7th July 2009</a><a href="http://www.millersmiles.co.uk/archives/97">28th June 2009 - 3rd July 2009</a><a href="http://www.millersmiles.co.uk/archives/96">27th June 2009 - 28th June 2009</a><a href="http://www.millersmiles.co.uk/archives/95">15th June 2009 - 27th June 2009</a><a href="http://www.millersmiles.co.uk/archives/94">29th May 2009 - 15th June 2009</a><a href="http://www.millersmiles.co.uk/archives/93">12th May 2009 - 29th May 2009</a><a href="http://www.millersmiles.co.uk/archives/92">26th April 2009 - 12th May 2009</a><a href="http://www.millersmiles.co.uk/archives/91">9th April 2009 - 26th April 2009</a><a href="http://www.millersmiles.co.uk/archives/90">24th March 2009 - 9th April 2009</a><a href="http://www.millersmiles.co.uk/archives/89">8th March 2009 - 24th March 2009</a><a href="http://www.millersmiles.co.uk/archives/88">19th February 2009 - 8th March 2009</a><a href="http://www.millersmiles.co.uk/archives/87">2nd February 2009 - 19th February 2009</a><a href="http://www.millersmiles.co.uk/archives/86">17th January 2009 - 2nd February 2009</a><a href="http://www.millersmiles.co.uk/archives/85">31st December 2008 - 17th January 2009</a><a href="http://www.millersmiles.co.uk/archives/84">14th December 2008 - 31st December 2008</a><a href="http://www.millersmiles.co.uk/archives/83">28th November 2008 - 14th December 2008</a><a href="http://www.millersmiles.co.uk/archives/82">12th November 2008 - 28th November 2008</a><a href="http://www.millersmiles.co.uk/archives/81">26th October 2008 - 11th November 2008</a><a href="http://www.millersmiles.co.uk/archives/80">8th October 2008 - 26th October 2008</a><a href="http://www.millersmiles.co.uk/archives/79">22nd September 2008 - 8th October 2008</a><a href="http://www.millersmiles.co.uk/archives/78">5th September 2008 - 21st September 2008</a><a href="http://www.millersmiles.co.uk/archives/77">19th August 2008 - 5th September 2008</a><a href="http://www.millersmiles.co.uk/archives/76">3rd August 2008 - 19th August 2008</a><a href="http://www.millersmiles.co.uk/archives/75">17th July 2008 - 2nd August 2008</a><a href="http://www.millersmiles.co.uk/archives/74">30th June 2008 - 17th July 2008</a><a href="http://www.millersmiles.co.uk/archives/73">14th June 2008 - 30th June 2008</a><a href="http://www.millersmiles.co.uk/archives/72">28th May 2008 - 13th June 2008</a><a href="http://www.millersmiles.co.uk/archives/71">12th May 2008 - 28th May 2008</a><a href="http://www.millersmiles.co.uk/archives/70">26th April 2008 - 12th May 2008</a><a href="http://www.millersmiles.co.uk/archives/69">9th April 2008 - 25th April 2008</a><a href="http://www.millersmiles.co.uk/archives/68">23rd March 2008 - 9th April 2008</a><a href="http://www.millersmiles.co.uk/archives/67">7th March 2008 - 23rd March 2008</a><a href="http://www.millersmiles.co.uk/archives/66">19th February 2008 - 6th March 2008</a><a href="http://www.millersmiles.co.uk/archives/65">2nd February 2008 - 19th February 2008</a><a href="http://www.millersmiles.co.uk/archives/64">17th January 2008 - 2nd February 2008</a><a href="http://www.millersmiles.co.uk/archives/63">31st December 2007 - 16th January 2008</a><a href="http://www.millersmiles.co.uk/archives/62">14th December 2007 - 31st December 2007</a><a href="http://www.millersmiles.co.uk/archives/61">28th November 2007 - 14th December 2007</a><a href="http://www.millersmiles.co.uk/archives/60">11th November 2007 - 27th November 2007</a></p>
	</html>
"""

extract_links_to_excel(html_code, 'main_links.xlsx')