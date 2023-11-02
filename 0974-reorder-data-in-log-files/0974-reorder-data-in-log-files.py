class Solution:
    def reorderLogFiles(self, logs):
        num_log = []
        str_log = []
        for log in logs:
            log = log.split(' ')
            if log[1][0] in '1234567890':
                num_log.append(log)
            else:
                str_log.append(log)

        str_log.sort(key=lambda x: (x[1:],x[0]))

        num_log_= [' '.join(x) for x in num_log]
        str_log_ = [' '.join(x) for x in str_log]
        
        return str_log_ + num_log_