from flask import Flask

FAI=Flask(__name__)

@FAI.route('/firststring')

def firststring():
    return 'This is Our First Flask Project'

if __name__=='__main__':
    FAI.run(debug=True)
