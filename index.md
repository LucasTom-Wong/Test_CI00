<h1>
  
  TedXSoftDev - Continous Integration by LTW
  
</h1>

<p>
  <h2>
  Continous integration is a useful practice for devos who work in groups 
  </h2>
  Steps for continous integration include but are not limited to: 
  <ul>
    <li>
      Updating a shared repository constantly with small but consistent changes <br>
    </li>
    <li>
      Always having a working base of code to develop on <br>
    </li>
    <li>
      Pulling the most recently updating code and always developing on the most recent design <br>
    </li>
  </ul>
</p>

<p>
  When a devo makes changes to a code, it becomes less and less like the original source code. As such, devos who are working on the same project will eventually branch out and merge conflicts may occur and they become more likely the longer changes are made without pushing it to the shared repository.  
</p>

<p>
  Continous integration fixes this issue by insuring that the shared repository is more likely to be:
  <ol>
    <li> Updated </li>
    <li> Working </li>
    <li> Compatible </li>
   </ol>
   Through continous integration, merge conflicts are less likely to exist, and are easier to detect and deal with.
</p>
  
<p>
  <h2>
    CI's partner in crime, is CD or continous deployment. <br>
  </h2>
  Continous deployment helps ensure that the shared base of code is testing constantly and regularly into to ensure workingness. <br>
  Typically continous integration and continous deployment are paired in a CI/CD pipeline. 
</p>

<p>
  CD can be facilitated by a variety of software or services including but not limited to:
  <ul>
    <li> Jenkins </li>
    <li> TravisCI </li>
    <li> CircleCI </li>
    <li> Github </li>
  </ul>
</p>

<p>
  I have done a little bit of testing with Github actions which can be found here: https://github.com/LucasTom-Wong/Test_CI00
</p>
