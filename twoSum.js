
// Variant 1

const input = [3, 4, 2, 4, 6]
const tar = 9

function twoSum(nums, target) {

	for (let i = 0; i < nums.length; i++) {
		for (let j = i + 1; j < nums.length; j++) {
			 if (nums[i] + nums[j] === target) {
					return {
						index: [i, j],
						value: [nums[i], nums[j]]
					}
			 }
		}
	}

}

const result = twoSum(input, tar)
console.log(result)

// Variant 2

function TwoSum(nums, target) {

	const map = new Map()

	for(let i = 0; i < nums.length; i++) {

		let diff = target - nums[i]
        
    if (map.has(diff)) {
    	return {
				index: [i, map.get(diff)],
				value: [nums[i], nums[map.get(diff)]]
			}
    }
        
    map.set(nums[i], i)

	}

}

const Result = TwoSum(input, tar)
console.log(Result)

