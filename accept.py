# https://boto.readthedocs.org/en/latest/ref/mturk.html
import boto.mturk.connection

sandbox_host = 'mechanicalturk.sandbox.amazonaws.com'
real_host = 'mechanicalturk.amazonaws.com'

mturk = boto.mturk.connection.MTurkConnection(
    aws_access_key_id = 'access key',
    aws_secret_access_key = 'secret key',
    host = real_host,
    debug = 1 # debug = 2 prints out all requests. but we'll just keep it at 1
)

def accept_assignments(assignments):
  print "starting to accept..."
  valid_response_ids = load_response_ids_from_csv()
  for assignment in assignments:
    # hits must be in order of completion
    response_id = get_answer_from_assignment(assignment).strip()
    assignment_id = assignment.AssignmentId
    if response_id in valid_response_ids:
      valid_response_ids.remove(response_id)  # mark as paid
      mturk.approve_assignment(assignment_id)
    else:
      print "rejected assignment id {} with response of {}".format(assignment_id, response_id)
      mturk.reject_assignment(assignment_id, feedback="Invalid response code - we will investigate further and fix if this was in error")

  print "done"
  print "left: {}".format(len(valid_response_ids))

def load_response_ids_from_csv():
  return set([
    "R_exPsDCgkCf8xcsR",
    "R_4PkVULYaW27rzEN",
    "R_9oSAaCpguWxIpVz",
    "R_eA5xbyLhUXM6QPH",
    "R_eEcGidJ446pVv7f",
    "R_8rgLZhI9T93nyFT",
    "R_cIkOOnofxqUpZWd",
    "R_9LxhFU50sPDoF1j",
    "R_3dzn00QYtL7jD5X",
    "R_2of1JrfQd8cOvdP",
    "R_d0TKiE9tJq2KzY1",
    "R_87kOoITN5DOXUSF",
    "R_5C35RXt9FCvv9Wt",
    "R_8GiNm4TfSOmhXrT",
    "R_6W11JDR256llZ4N",
    "R_5nVLakixHidIoD3",
    "R_5ySVdZiST8j0nZP",
    "R_4ZOQP5YAUwWX4a1",
    "R_6JrG65P71pPRILb",
    "R_doGFiyrWxnpIy4R",
    "R_e9w1fzio934iEtf",
    "R_3t6znhr8CmW6col",
    "R_etvOKlfAfjX1153",
    "R_5hCehgBPFBFbe2V",
    "R_1B1DEWHsThHltFX",
    "R_0ewBvEYZaYARVdz",
    "R_2tmKBg6lOHTSBSZ",
    "R_cUz5TjQ0qE66TvT",
    "R_6YGrXLXS6wwCFCt",
    "R_4SLbMmiuHPyrKbX",
    "R_822XGtm3lWrQVIF",
    "R_1XG5HCS3vXIc0x7",
    "R_0HErJ2RjKTN0BPD",
    "R_72ofsYLW9nDIpmt",
    "R_1OdF0YZPrIZzi29",
    "R_8pqFgN9GqSGv6QJ",
    "R_1H1vl4dQvbaf9DD",
    "R_6upkeiBkcH9TVJ3",
    "R_6gssaTfzXWmzZcx",
    "R_5psKD9RP4UzvFEV",
    "R_a5b4ZFAUs2ATRSl",
    "R_74h9zdoOOAXqqsR",
    "R_9mqbp6sPBJN0DyZ",
    "R_cHDkIyb6xIuXfWR",
    "R_bPMkIXjaqRW0kLj",
    "R_8GgViJLkIeIiM8B",
    "R_1Fblwj26wUybrRX",
    "R_55vAlI4x6kCcApD",
    "R_b1tl5SdapHoeb8V",
    "R_85DpngMfYbWAii1",
    "R_doPUydK84MmajwF",
    "R_9EoqR7FTznOes3b",
    "R_2ltuwDQaRA54dpj",
    "R_9owp5w1i5JpTnTv",
    "R_6ssd0UkAF0l0xG5",
    "R_9YzmpBzHJtnedVz",
    "R_e4Ms9gQqiZ5WY85",
    "R_6RVxRPbxJpbfr01",
    "R_blxtLtmyDuhdrlr",
    "R_bqDtyGOOAGqyKSF",
    "R_0ueqsIUNXVwmFBX",
    "R_cHHbJJubagtNSpn",
    "R_3wp97ODP6nXBUQB",
    "R_eQZWZ0VAMitW0iF",
    "R_0rD9ibkbvYCgEgB",
    "R_ba9LF6tdoNaDYeF",
    "R_1HUE70B4O3Ts3iJ",
    "R_3lX8JDtnPvsXo6F",
    "R_74hkA2L7uh4YzqJ",
    "R_agvAK4oW0YtwvD7",
    "R_2uxQuYU3uEO6V5X",
    "R_9NTFDvSgd9lL3Kt",
    "R_1Ye5H7L2PveFVNb",
    "R_5zF3oLZnJG4IcrH",
    "R_3ER2jqwl4zAc8cZ",
    "R_09i0qfKyUqHvmPr",
    "R_abegfnCgiV8oUCh",
    "R_5aVfBfBCQ5yRG3b",
    "R_agivC7evkneVWvz",
    "R_3t2hU4eS5qdo48R",
    "R_bCVRqXN02HGd1Rj",
    "R_ezgAEzYT2AsarNb",
    "R_6Qk51icjwB977ZH",
    "R_4Ui4f1psDsLBHU1",
    "R_cAaHVeLfzl10XvD",
    "R_e33OL3UBje07UcR",
    "R_eSgDwFwAaR4EXqJ",
    "R_3lzDnvOyqVdQQRf",
    "R_0odbgnCZ1lYTTdr",
    "R_79EpMDlfTck9fq5",
    "R_8xks5Yd8kWLeKlT",
    "R_8AiBS19t6lPofxX",
    "R_3W1hyahb3N9I8V7",
    "R_6GnSIyjKcCdE99z",
    "R_1Opgm8MrOLzqTAN",
    "R_daNXVQP66HIdBpH",
    "R_e355nSvLUuAYHLn",
    "R_5cGFGrW6pKvawnj",
    "R_3dQwRFit9p9jolT",
    "R_8oWVxlUQlLq5FfD",
    "R_b3kXrjz6EzCAD3f",
    "R_2hIWpofiVAU0P9b",
    "R_6RO7FnYF5y8hp9X",
    "R_0iEzwbcDm4XFpJj",
    "R_3l91yblOQWPh9YN",
    "R_1G4vH1wTEONx2F7",
    "R_a4qy92Oq9ecOCFf",
    "R_5Bwe9UOLnbqi19z",
    "R_6SfzBKVwo8ixufj",
    "R_6VAMQg9GPsavrwN",
    "R_0MKYtqbDj62fsb3",
    "R_af545aNfxFvADxX",
    "R_9yPSsGZHvniuBSd",
    "R_1IdYrGReEhuJbA9",
    "R_4TREFLUBZA6rN2Z",
    "R_b2XSg5L3XztMGXz",
    "R_ehd6cL7bOh5Gnt3",
    "R_cM7DWgUdgGP1RkN",
    "R_4ZalRv1kRAiekap",
    "R_cYd5JOd8I3gGifb",
    "R_1TgMfyxyU9qb1S5",
    "R_0x1SLxGftKxAIvz",
    "R_0GwOjqhEg7iAJed",
    "R_cuT1ZzUAICGF5n7",
    "R_8phGRIWUiiZ54ON",
    "R_0lnjopykipLhNrL",
    "R_eh5ACs8uD9mnWkZ",
    "R_dhABalqG8b3Lm6x",
    "R_b7AGVhMb57ZMCDb",
    "R_bHn2997cpzpyQJL",
    "R_3PGZcjn9G3SG8ip",
    "R_bkqMaLKJVoHus9D",
    "R_e3gZUv9gQsjdHSZ",
    "R_5axM4lO4cE1pO97",
    "R_ddsbIgDnZTKUxrT",
    "R_9FB5PkGxca0Ns8J",
    "R_8k5KYTwiSBI0dLf",
    "R_emqGHhrcW6m2obH",
    "R_8olfJryqQPHCbB3",
    "R_d3TUB3rRhucyn53",
    "R_3UXdOFM6huAwf5j",
    "R_23qzIZCYSz4M6dD",
    "R_6EGklcosc4o1vAp",
    "R_9HX8MlBqrnGiUyV",
    "R_0xHpQaesamm0o7j",
    "R_aid6z6GuJqCvYAR",
    "R_4VkU1IhTLOYdCdL",
    "R_3Po7S0tK52vHQ7H",
    "R_a4WDqk4thGGMSs5",
    "R_erhyHU21V0HQnS5",
    "R_7PP1g3ksb1wLQX3",
    "R_bf2WrtSNWpXV9OZ",
    "R_8HzyBc1isEYzoSF",
    "R_3PLzEELmDU75Ped",
    "R_e5mfBvd3keW1WkJ",
    "R_3vEKShRHYRFIMuN",
    "R_0vPsZPdnne33fCZ",
    "R_a4xH3TawnghLwXz",
    "R_6s4kB2aZ7mk59TT",
    "R_4YHSbySW3nQM4Yd",
    "R_6rOelyDdu8gU83H",
    "R_bxZQupdJRI0Xd2J",
    "R_b16b7VbfEsH29et",
    "R_6mbPCmBlyDJv4pL",
    "R_do6CgNxuh3SAdox",
    "R_7UNGoXNoWmyWTOZ",
    "R_5yuSPTdTDIgWOvb",
    "R_b2VAzhMzIagRP3D",
    "R_23Pcbc2W0Aaddyt",
    "R_d5TWYHMivHMfZid",
    "R_1Hue3tFTvalxprf",
    "R_eeQsmjGw1c5ebmB",
    "R_b8gGIgCL4E600Pb",
    "R_bK0TkksrNSdAG3P",
    "R_3ehD42EcUhOtlR3",
    "R_enG1nAmFW9ZlcFv",
    "R_brAaZx4uwlvUs9n",
    "R_cMSdWKiIVEw7sbz",
    "R_dbsftHRY1sxk4ND",
    "R_3IvRmEKD631Vlcx",
    "R_er0mnMuoU1C7O61",
    "R_0MTBPI1bsRjneMl",
    "R_bHkivj1sez3nmOV",
    "R_bC3No5qHLacqHYx",
    "R_efXmJ1vqJmqeW2N",
    "R_6Kyu4D2FCH7QfeR",
    "R_cNjKPmkpSO9JFIh",
    "R_bwTVhmH8MhXWBZH",
    "R_bscB6PaNt9VUXEV",
    "R_doKeeHcPz2lZOkZ",
    "R_893WBxK2v94v7y5",
    "R_cYgOscJoqsEV9yJ",
    "R_8wivxmpz2nWeOG1",
    "R_7OgL4pxCkNiUMy9",
    "R_ehWAPXKAJu5CYvP",
    "R_5swFTnhZgi52COh",
    "R_1YXdc5o4oBhF1NX",
    "R_8InFVAQeFsB9blX",
    "R_aVIqKwcYUXM672Z",
    "R_diNsZVysZvTjKdL",
    "R_a5UUtcniIxTV9rf",
    "R_b7untfpKdCb47cN",
  ])

def get_answer_from_assignment(assignment):
  return assignment.answers[0][0].fields[0]

def get_all_assignments(hit_id):
  result = []
  total_num_result = int(mturk.get_assignments(hit_id, page_size=1).TotalNumResults)
  pages = range(1, 1 + total_num_result / 100)
  for page in pages:
    result += mturk.get_assignments(hit_id, page_size=100, page_number=page)

  return result

def main():
  all_assignments = get_all_assignments("3ZG552ORAM4IRP7XEMODPMOIGLU2VV")
  accept_assignments(all_assignments)

main()
